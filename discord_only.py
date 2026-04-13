from dotenv import load_dotenv 
import os
import discord
import openai
from discord.ext import commands
load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

client = discord.Client(intents=intents)
async def on_ready():
    print(f'We have logged in as {client.user}')
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')    


openai.api_key = os.getenv("OPENAI_API_KEY")

if message.content.endswith('question'):

response = openai.ChatCompletion.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": "Hello, please respond with a short message on {message.content}."}
    ],
)
client.run(os.getenv('DSCBOTTOKEN'))
