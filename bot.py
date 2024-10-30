import os
import discord
from dotenv import load_dotenv
from discord.ext import commands


# Load environment variables from .env file
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
OWNER_ID = os.getenv("OWNER_ID")


# Initialize bot with command prefix and intents
intents = discord.Intents.default()
intents.message_content = True  # Required for reading messages
bot = commands.Bot(command_prefix="!", intents=intents)


# Command to manually sync slash commands
@bot.command(name="sync")
async def sync(ctx):
    if ctx.author.id != int(OWNER_ID):
        await ctx.send(
            "Nope. I only listen to my owner when it comes to serious business."
        )
        return

    await ctx.send("Syncing slash commands...")  # Inform the user that sync is starting
    try:
        await bot.tree.sync()
        await ctx.send("Slash commands have been synced successfully!")
        print("Slash commands synced successfully.")  # Debug statement
    except Exception as e:
        await ctx.send(f"An error occurred while syncing commands: {e}")
        print(f"Error syncing commands: {e}")  # Debug statement


# Sync commands and confirm bot is ready
@bot.event
async def on_ready():
    print(f"{bot.user} Yawnsss... I'm awake!")

    for filename in os.listdir("cogs"):  # for every cog in the cogs folder
        if filename[-1] == "y":
            # ^^ If the cog ends in "y", checking if it's a python file
            try:
                await bot.load_extension(f"cogs.{filename[:-3]}")
            except Exception:
                pass  # Maybe do something here, not sure
    """
    try:
        await bot.tree.sync()
        print("Slash commands synced.")
        # Debug: print all registered commands
        for command in bot.tree.get_commands():
            print(f"Synced command: {command.name}")
    except Exception as e:
        print(f"Error syncing slash commands: {e}")
    """

# Run bot
bot.run(TOKEN)
