import discord
from discord.ext import commands
import random

class SekizTop(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="8ball", aliases=["sekiz-top"])
    async def sekiz_top(self, ctx, *, soru: str):
        cevaplar = [
            "Kesinlikle evet.", "Görünüşe göre öyle.", "Şüphesiz.", "Büyük ihtimalle.", 
            "Buna güvenebilirsin.", "Şu an tahmin edemiyorum, tekrar sor.", "Daha sonra tekrar sor.",
            "Bunu şimdi söylemesem daha iyi.", "Konsantre ol ve tekrar sor.", "Buna pek bel bağlama.",
            "Benim cevabım hayır.", "Kaynaklarım hayır diyor.", "Pek iyi görünmüyor.", "Çok şüpheli."
        ]
        
        embed = discord.Embed(title="🎱 Sihirli 8 Top", color=discord.Color.darker_grey())
        embed.add_field(name="Soru:", value=f"*{soru}*", inline=False)
        embed.add_field(name="Cevap:", value=f"**{random.choice(cevaplar)}**", inline=False)
        
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(SekizTop(bot))