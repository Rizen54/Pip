import discord
import os
from dotenv import load_dotenv


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'I\'m awake as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower().startswith('!hi') or message.content.lower().startswith('!hello'):
        await message.channel.send('Hello!')


load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
client.run(TOKEN)
