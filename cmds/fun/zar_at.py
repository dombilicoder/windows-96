import discord
from discord.ext import commands
import random

class ZarAt(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="zar-at", aliases=["zarat", "roll"])
    async def zar_at(self, ctx):
        sayi = random.randint(1, 6)
        embed = discord.Embed(title="🎲 Zar Atıldı!", description=f"Gelen Sayı: **{sayi}**", color=discord.Color.blurple())
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(ZarAt(bot))