import discord
from discord.ext import commands

class Yardim(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="yardım", aliases=["yardim", "help"])
    async def yardim(self, ctx: commands.Context):
        embed = discord.Embed(
            title="💾 Windows 96 - Sistem Yardım Menüsü",
            description="Aşağıda kullanabileceğin tüm komutlar kategorilerine göre listelenmiştir.",
            color=discord.Color.teal()
        )

        # --- MÜZİK KOMUTLARI ---
        muzik_komutlari = (
            "`w.oynat <şarkı>`: İstediğin şarkıyı arar, detaylı panel açarak çalar.\n"
            "`w.dur`: Çalan şarkıyı anlık duraklatır (Sessiz çalışır).\n"
            "`w.devam`: Duraklatılan şarkıyı sürdürür (Sessiz çalışır).\n"
            "`w.sar <saniye>`: Şarkıyı belirtilen saniye kadar ileri sarar.\n"
            "`w.geç`: Çalan şarkıyı atlar, sıradakine geçer.\n"
            "`w.sıra`: O anki aktif müzik sırasını listeler.\n"
            "`w.ses <0-500>`: Seviyeyi ayarlar ve canlı paneli günceller.\n"
            "`w.bitir`: Müziği tamamen kapatır ve sırayı temizler."
        )
        embed.add_field(
            name="<a:kelof_music:1233845355498442953> Müzik Komutları",
            value=muzik_komutlari,
            inline=False
        )

        # --- GENEL KOMUTLAR ---
        genel_komutlari = (
            "`w.yardım`: Bu yardım menüsünü gösterir.\n"
            "`w.emoji`: Sunucudaki tüm emojileri ID'leri ile birlikte listeler."
        )
        embed.add_field(
            name="📖 Genel Komutlar",
            value=genel_komutlari,
            inline=False
        )

        # --- MODERASYON KOMUTLARI ---
        mod_komutlari = (
            "`w.sil <miktar>`: Kanaldaki mesajları toplu olarak siler. *(Maks: 100)*"
        )
        embed.add_field(
            name="<a:kelof_develop:1233880260223959192> Moderasyon Komutları",
            value=mod_komutlari,
            inline=False
        )

        embed.set_footer(
            text=f"Sorgulayan: {ctx.author.name} | Windows 96", 
            icon_url=ctx.author.display_avatar.url
        )

        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Yardim(bot))