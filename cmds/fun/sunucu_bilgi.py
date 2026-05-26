import discord
from discord.ext import commands

class SunucuBilgi(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Hata buradaydı: aliases içinden "sunucu-bilgi" çıkarıldı
    @commands.command(name="sunucu-bilgi", aliases=["serverinfo"])
    async def sunucu_bilgi(self, ctx):
        guild = ctx.guild
        embed = discord.Embed(title=f"🏰 Sunucu Bilgisi: {guild.name}", color=discord.Color.gold())
        if guild.icon:
            embed.set_thumbnail(url=guild.icon.url)
            
        embed.add_field(name="Sunucu Sahibi", value=f"<@{guild.owner_id}>", inline=True)
        embed.add_field(name="Üye Sayısı", value=f"`{guild.member_count}`", inline=True)
        embed.add_field(name="Kanal Sayısı", value=f"`{len(guild.channels)}`", inline=True)
        embed.add_field(name="Rol Sayısı", value=f"`{len(guild.roles)}`", inline=True)
        embed.add_field(name="Kuruluş Tarihi", value=f"<t:{int(guild.created_at.timestamp())}:D>", inline=True)
        
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(SunucuBilgi(bot))