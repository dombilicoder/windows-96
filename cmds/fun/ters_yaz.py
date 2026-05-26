import discord
from discord.ext import commands

class TersYaz(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Hata buradaydı: aliases içinden "ters-yaz" çıkarılıp "tersyaz" yapıldı
    @commands.command(name="ters-yaz", aliases=["tersyaz", "reverse"])
    async def ters_yaz(self, ctx, *, metin: str):
        ters = metin[::-1]
        embed = discord.Embed(title="🔁 Ters Metin", description=f"`{ters}`", color=discord.Color.teal())
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(TersYaz(bot))