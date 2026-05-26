import discord
from discord.ext import commands

class Ban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ban", aliases=["yasakla"])
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, sebep="Belirtilmedi"):
        await member.ban(reason=sebep)
        embed = discord.Embed(title="🚫 Kullanıcı Yasaklandı", description=f"**Yasaklanan:** {member.mention}\n**Yetkili:** {ctx.author.mention}\n**Sebep:** {sebep}", color=discord.Color.red())
        await ctx.send(embed=embed, delete_after=10)
        try: await ctx.message.delete()
        except: pass

async def setup(bot):
    await bot.add_cog(Ban(bot))