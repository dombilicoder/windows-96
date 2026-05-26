import discord
from discord.ext import commands

class Yavasmod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="yavaşmod", aliases=["slowmode"])
    @commands.has_permissions(manage_channels=True)
    async def yavasmod(self, ctx, saniye: int):
        await ctx.channel.edit(slowmode_delay=saniye)
        embed = discord.Embed(title="⏱️ Yavaş Mod Ayarlandı", description=f"Bu kanalda artık **{saniye}** saniyede bir mesaj gönderilebilecek.", color=discord.Color.blue())
        if saniye == 0:
            embed.description = "Yavaş mod bu kanal için tamamen kapatıldı."
        await ctx.send(embed=embed, delete_after=10)
        try: await ctx.message.delete()
        except: pass

async def setup(bot):
    await bot.add_cog(Yavasmod(bot))