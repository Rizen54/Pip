import random

import discord
from discord import app_commands
from discord.ext import commands


class Cafe(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot


    @app_commands.command(name="menu", description="Displays cafe menu.")
    async def menu(self, interaction: discord.Interaction):
        """Displays a list of available Food items in the cafe."""
    
        menu_list = [
            ":coffee: *Coffee* - `Free`",
            ":sandwich: *Sandwich*- `$4`",
            ":pizza: *Pizza* - `$5`",
            ":hamburger: *Burger* - `$3`",
        ]

        embed = discord.Embed(
            title="📜 ***Cafe Menu***",
            description="What would you like to have?",
            color=discord.Color.dark_gold(),
        )

        embed.add_field(name="Options", value="\n".join(menu_list), inline=False)
        await interaction.response.send_message(embed=embed)


    @app_commands.command(name="order", description="Places order for a food item.")
    async def order(self, interaction: discord.Interaction, option: str):
        menu = {"coffee": "free", "sandwich": "$4", "burger": "$3", "pizza": "$5"}
        if option.lower() in menu:
            await interaction.response.send_message(f"Here's your *{option.capitalize()}* for `{menu[option]}`!")
        

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Cafe(bot))
