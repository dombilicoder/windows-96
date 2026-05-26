import discord
from discord.ext import commands

class Isim(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="isim", aliases=["nick"])
    @commands.has_permissions(manage_nicknames=True)
    async def isim(self, ctx, member: discord.Member, *, yeni_isim: str):
        old_name = member.display_name
        await member.edit(nick=yeni_isim)
        embed = discord.Embed(title="📝 İsim Değiştirildi", description=f"**Kullanıcı:** {member.mention}\n**Eski İsim:** `{old_name}`\n**Yeni İsim:** `{yeni_isim}`", color=discord.Color.teal())
        await ctx.send(embed=embed, delete_after=10)
        try: await ctx.message.delete()
        except: pass

async def setup(bot):
    await bot.add_cog(Isim(bot))