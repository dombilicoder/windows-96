import discord
from discord.ext import commands

class Unban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="unban", aliases=["yasakkaldır"])
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, user_id: int):
        user = await self.bot.fetch_user(user_id)
        await ctx.guild.unban(user)
        embed = discord.Embed(title="✅ Yasak Kaldırıldı", description=f"**Yasağı Kaldırılan:** {user.name}\n**Yetkili:** {ctx.author.mention}", color=discord.Color.green())
        await ctx.send(embed=embed, delete_after=10)
        try: await ctx.message.delete()
        except: pass

async def setup(bot):
    await bot.add_cog(Unban(bot))