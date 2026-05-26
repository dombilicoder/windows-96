import discord
from discord.ext import commands

class RolAl(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="rol-al", aliases=["role-remove"])
    @commands.has_permissions(manage_roles=True)
    async def rol_al(self, ctx, member: discord.Member, role: discord.Role):
        await member.remove_roles(role)
        embed = discord.Embed(title="💼 Rol Alındı", description=f"**Kullanıcı:** {member.mention}\n**Alınan Rol:** {role.mention}\n**Yetkili:** {ctx.author.mention}", color=discord.Color.dark_blue())
        await ctx.send(embed=embed, delete_after=10)
        try: await ctx.message.delete()
        except: pass

async def setup(bot):
    await bot.add_cog(RolAl(bot))