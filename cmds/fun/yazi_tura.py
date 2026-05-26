import discord
from discord.ext import commands
import random

class YaziTura(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="yazı-tura", aliases=["yazi-tura", "coinflip"])
    async def yazi_tura(self, ctx):
        sonuc = random.choice(["Yazı", "Tura"])
        embed = discord.Embed(title="🪙 Para Atıldı!", description=f"Gelen: **{sonuc}**", color=discord.Color.gold())
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(YaziTura(bot))