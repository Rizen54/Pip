import discord
import os
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
OWNER_ID = os.getenv("OWNER_ID")


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
async def sync(ctx):
    if ctx.author.id != OWNER_ID:
        await ctx.send("Nope. I only listen to my owner when it comes to serious business.")
        return

    await ctx.send("Syncing slash commands...")  # Inform the user that sync is starting
    try:
        await bot.tree.sync()
        await ctx.send("Slash commands have been synced successfully!")
        print("Slash commands synced successfully.")  # Debug statement
    except Exception as e:
        await ctx.send(f"An error occurred while syncing commands: {e}")
        print(f"Error syncing commands: {e}")  # Debug statement


@bot.tree.command(name="commands", description="Lists all the bot commands.")
async def list_commands(interaction: discord.Interaction):
    """Displays a list of available commands in an embed."""
    commands_list = [f"`/{command.name}` - {command.description or 'No description'}" for command in bot.tree.get_commands()]

    embed = discord.Embed(
        title="📜 Available Commands",
        description="Here’s what I can do for you!",
        color=discord.Color.purple()
    )

    embed.add_field(name="Commands", value="\n".join(commands_list), inline=False)
    await interaction.response.send_message(embed=embed)


# Sync commands and confirm bot is ready
@bot.event
async def on_ready():
    print(f"{bot.user} Yawnsss... I'm awake!")
    try:
        await bot.tree.sync()
        print("Slash commands synced.")
        # Debug: print all registered commands
        for command in bot.tree.get_commands():
            print(f"Synced command: {command.name}")
    except Exception as e:
        print(f"Error syncing slash commands: {e}")


# Run bot
bot.run(TOKEN)
