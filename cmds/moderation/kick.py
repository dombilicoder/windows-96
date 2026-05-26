import discord
from discord.ext import commands

class Kick(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="kick", aliases=["at"])
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, sebep="Belirtilmedi"):
        await member.kick(reason=sebep)
        embed = discord.Embed(title="🔨 Kullanıcı Atıldı", description=f"**Atılan:** {member.mention}\n**Yetkili:** {ctx.author.mention}\n**Sebep:** {sebep}", color=discord.Color.orange())
        await ctx.send(embed=embed, delete_after=10)
        try: await ctx.message.delete()
        except: pass

async def setup(bot):
    await bot.add_cog(Kick(bot))