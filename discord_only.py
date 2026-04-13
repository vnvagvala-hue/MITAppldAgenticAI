from dotenv import load_dotenv 
import os
import discord
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

client.run(os.getenv('DSCBOTTOKEN'))