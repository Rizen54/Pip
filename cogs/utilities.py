import random

import discord
from discord import app_commands
from discord.ext import commands


class Utilities(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot


    @app_commands.command(name="commands", description="Lists all the bot commands.")
    async def list_commands(self, interaction: discord.Interaction):
        """Displays a list of available commands in an embed."""
        commands_list = [
            f"`/{command.name}` - {command.description or 'No description'}"
            for command in self.bot.tree.get_commands()
        ]

        embed = discord.Embed(
            title="📜 Available Commands",
            description="Here’s what I can do for you!",
            color=discord.Color.purple(),
        )

        embed.add_field(name="Commands", value="\n".join(commands_list), inline=False)
        await interaction.response.send_message(embed=embed)


    @app_commands.command(name="hi", description="The bot says hi!")
    async def say_hi(self, interaction: discord.Interaction):
        await interaction.response.send_message("Hello!")


    @app_commands.command(name="flip", description="Flips a coin.")
    async def flip_coin(self, interaction: discord.Interaction):
        """Flips a coin!"""
        await interaction.response.send_message(random.choice(["Heads!", "Tails!"]))
    
    @app_commands.command(name="choose", description="Randomly chooses an option from a list.")
    async def choose(self, interaction: discord.Interaction, options: str):
        """Choose one random item from a list of options."""
        # Split the options by spaces
        choices = options.split()
        
        # Check if there are at least two options
        if len(choices) == 1:
            await interaction.response.send_message("Are you so choosy that you can't choose from a single option??")
            return
        
        # Randomly choose an option
        chosen_option = random.choice(choices)
        await interaction.response.send_message(f"I choose **{chosen_option}!**")


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Utilities(bot))
