import discord
from discord.ext import commands
import random

class KacCm(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="kaç-cm", aliases=["kac-cm", "ppsize"])
    async def kac_cm(self, ctx, user: discord.Member = None):
        user = user or ctx.author
        uzunluk = random.randint(1, 35)
        bar = "=" * uzunluk
        
        embed = discord.Embed(title="📏 Ölçüm Merkezi", description=f"**{user.display_name}** adlı kişinin aleti:\n\n8{bar}D\n`{uzunluk} cm`", color=discord.Color.dark_theme())
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(KacCm(bot))