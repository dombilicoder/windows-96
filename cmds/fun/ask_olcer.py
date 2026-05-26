import discord
from discord.ext import commands
import random

class AskOlcer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="aşk-ölçer", aliases=["ask-olcer", "love"])
    async def ask_olcer(self, ctx, user1: discord.Member, user2: discord.Member = None):
        if user2 is None:
            user2 = ctx.author
            
        yuzde = random.randint(0, 100)
        
        if yuzde < 30: mesaj = "Pek umut yok gibi..."
        elif yuzde < 60: mesaj = "Bir kahve içilebilir."
        elif yuzde < 90: mesaj = "Mükemmel bir uyum!"
        else: mesaj = "Siz evlenmelisiniz! 💍"

        embed = discord.Embed(title="💘 Aşk Ölçer", description=f"{user1.mention} ve {user2.mention} arasındaki aşk seviyesi:", color=discord.Color.fuchsia())
        embed.add_field(name=f"Uyum: %{yuzde}", value=f"*{mesaj}*", inline=False)
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(AskOlcer(bot))