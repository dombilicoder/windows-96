import discord
from discord.ext import commands

class KilitAc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="kilit-aç", aliases=["unlock"])
    @commands.has_permissions(manage_channels=True)
    async def kilit_ac(self, ctx):
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=None)
        embed = discord.Embed(title="🔓 Kanal Kilidi Açıldı", description="Bu kanal tekrar mesaj gönderimine açılmıştır.", color=discord.Color.green())
        await ctx.send(embed=embed)
        try: await ctx.message.delete()
        except: pass

async def setup(bot):
    await bot.add_cog(KilitAc(bot))