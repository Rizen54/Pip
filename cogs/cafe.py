import random

import discord
from discord import app_commands
from discord.ext import commands


class Cafe(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot


    @app_commands.command(name="menu", description="Displays cafe menu.")
    async def menu(self, interaction: discord.Interaction):
        """Displays a list of available commands in an embed."""
    
        menu_list = [
        "*Coffee* - `$5`",
        "*Sandwiches* - `$7`",
        "*Burger* - `$3`",
        ]

        embed = discord.Embed(
            title="📜 𝓶𝓮𝓷𝓾",
            description="What would you like to have?!",
            color=discord.Color.brand_red(),
        )

        embed.add_field(name="Options", value="\n".join(menu_list), inline=False)
        await interaction.response.send_message(embed=embed)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Cafe(bot))
