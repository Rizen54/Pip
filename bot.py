import discord
import os
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")


# Initialize bot with command prefix and intents
intents = discord.Intents.default()
intents.message_content = True  # Required for reading messages
bot = commands.Bot(command_prefix="!", intents=intents)


# Define a slash command to say hi
@bot.tree.command(name="hi", description="The bot says hi!")
async def say_hi(interaction: discord.Interaction):
    await interaction.response.send_message("Hello!")


# Command to manually sync slash commands
@bot.command(name="sync")
@commands.is_owner()  # Only the bot owner can use this command
async def sync_slash_commands(ctx):
    await ctx.send("Syncing slash commands...")  # Inform the user that sync is starting
    try:
        await bot.tree.sync()
        await ctx.send("Slash commands have been synced successfully!")
        print("Slash commands synced successfully.")  # Debug statement
    except Exception as e:
        await ctx.send(f"An error occurred while syncing commands: {e}")
        print(f"Error syncing commands: {e}")  # Debug statement


# Command to list registered commands
@bot.command(name="commands")
async def list_commands(ctx):
    """Lists all registered commands."""
    commands_list = [command.name for command in bot.commands]
    await ctx.send("Registered commands: " + ", ".join(commands_list))


# Sync commands and confirm bot is ready
@bot.event
async def on_ready():
    print(f"{bot.user} Yawnsss... I am awake!")


# Run bot
bot.run(TOKEN)

