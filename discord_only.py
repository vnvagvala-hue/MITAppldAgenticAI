pwdfrom dotenv import load_dotenv
import os
import discord
from openai import OpenAI

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

openai_model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
openai_api_key = os.getenv("OPENAI_API_KEY")
openai_client = OpenAI(api_key=openai_api_key)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

async def get_openai_response(content):
    try:
        response = openai_client.chat.completions.create(
            model=openai_model,
            messages=[
                {"role": "user", "content": f"Hello, please respond with a short message on {content}."}
            ],
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error with OpenAI API: {e}")
        return "Sorry, I couldn't process your request."

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')
    elif message.content.startswith('Hello question:') \
        or message.content.startswith('Hello question:') \
          or message.content.startswith('hello question:') \
            or message.content.startswith('Hi question:') \
             or message.content.startswith('Hi Question:') \
              or message.content.startswith('hi question:') \
                or message.content.startswith('Question:') \
                    or message.content.startswith('question:'):
        response = await get_openai_response(message.content)
        await message.channel.send(response)
    else:
        await message.channel.send("Please start your message with 'Hello question:' \
                                  or 'Hi question:' or 'Question:' to get a response \
                                   from the bot.")

try:
    client.run(os.getenv('DSCBOTTOKEN'))
except Exception as e:
    print(f"Error starting the bot: {e}")
