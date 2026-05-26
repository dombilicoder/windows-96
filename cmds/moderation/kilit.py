import discord
from discord.ext import commands

class Kilit(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="kilit", aliases=["lock"])
    @commands.has_permissions(manage_channels=True)
    async def kilit(self, ctx):
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
        embed = discord.Embed(title="🔒 Kanal Kilitlendi", description="Bu kanal yeni bir emre kadar mesaj gönderimine kapatılmıştır.", color=discord.Color.red())
        await ctx.send(embed=embed)
        try: await ctx.message.delete()
        except: pass

async def setup(bot):
    await bot.add_cog(Kilit(bot))