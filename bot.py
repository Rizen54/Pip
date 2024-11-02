import os
import discord
from dotenv import load_dotenv
from discord.ext import tasks, commands


# Load environment variables from .env file
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
OWNER_ID = os.getenv("OWNER_ID")


# Initialize bot with command prefix and intents
intents = discord.Intents.default()
intents.message_content = True  # Required for reading messages
activity = discord.Activity(type=discord.ActivityType.watching, name="A Good Girl's Guide To Murder.")
bot = commands.Bot(command_prefix="!", intents=intents, activity=activity)


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

# Reloads all cogs
@bot.command(name="reload")
async def reload(ctx):
    if ctx.author.id != int(OWNER_ID):
        await ctx.send(
            "Nope. I only listen to my owner when it comes to serious business."
        )
        return

    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            cog_name = f"cogs.{filename[:-3]}"
            await bot.unload_extension(cog_name)
            try:
                await bot.load_extension(cog_name)
            except Exception as e:
                await ctx.send(f"Failed to load `{cog_name}`: {e}")

    await ctx.send("All cogs reloaded successfully.")



# Sync commands and confirm bot is ready
@bot.event
async def on_ready():
    print(
r"""
 ____  _  ____ 
/  __\/ \/  __\
|  \/|| ||  \/|
|  __/| ||  __/
\_/   \_/\_/   
               
"""
    )
    print(f"{bot.user} Yawnsss... I'm awake!")

    for filename in os.listdir("cogs"):  # for every cog in the cogs folder
        if filename.endswith(".py"):
            # ^^ If the cog ends in "y", checking if it's a python file
            try:
                await bot.load_extension(f"cogs.{filename[:-3]}")
            except Exception as e:
                print(e)
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
