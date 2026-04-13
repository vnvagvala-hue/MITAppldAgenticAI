from dotenv import load_dotenv
import os
import discord
import openai
from discord.ext import commands

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
#bot = commands.Bot(command_prefix='!', intents=intents)
client = discord.Client(intents=intents)

openai_model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
openai_api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = openai_api_key

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

async def get_openai_response(content):
    try:
        response = openai.ChatCompletion.create(
            model=openai_model,
            messages=[
                {"role": "user", "content": f"Hello, please respond with a short message on {content}."}
            ],
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        print(f"Error with OpenAI API: {e}")
        return "Sorry, I couldn't process your request."

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')
    elif message.content.endswith('question'):
        response = await get_openai_response(message.content)
        await message.channel.send(response)

try:
    client.run(os.getenv('DSCBOTTOKEN'))
except Exception as e:
    print(f"Error starting the bot: {e}")
client.run(os.getenv('DSCBOTTOKEN'))
