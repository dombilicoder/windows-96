import discord
from discord.ext import commands

class RolVer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="rol-ver", aliases=["role-add"])
    @commands.has_permissions(manage_roles=True)
    async def rol_ver(self, ctx, member: discord.Member, role: discord.Role):
        await member.add_roles(role)
        embed = discord.Embed(title="💼 Rol Verildi", description=f"**Kullanıcı:** {member.mention}\n**Verilen Rol:** {role.mention}\n**Yetkili:** {ctx.author.mention}", color=discord.Color.blue())
        await ctx.send(embed=embed, delete_after=10)
        try: await ctx.message.delete()
        except: pass

async def setup(bot):
    await bot.add_cog(RolVer(bot))