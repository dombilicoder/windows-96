import discord
from discord.ext import commands

class SusturAc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="sustur-aç", aliases=["untimeout", "unmute"])
    @commands.has_permissions(moderate_members=True)
    async def sustur_ac(self, ctx, member: discord.Member):
        await member.timeout(None)
        embed = discord.Embed(title="🔊 Susturma Kaldırıldı", description=f"**Susturması Açılan:** {member.mention}\n**Yetkili:** {ctx.author.mention}", color=discord.Color.green())
        await ctx.send(embed=embed, delete_after=10)
        try: await ctx.message.delete()
        except: pass

async def setup(bot):
    await bot.add_cog(SusturAc(bot))