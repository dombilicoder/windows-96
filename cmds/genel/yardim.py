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
            "`w.dur`: Çalan şarkıyı anlık duraklatır.\n"
            "`w.devam`: Duraklatılan şarkıyı sürdürür.\n"
            "`w.sar <saniye>`: Şarkıyı belirtilen saniye kadar ileri sarar.\n"
            "`w.geç`: Çalan şarkıyı atlar, sıradakine geçer.\n"
            "`w.döngü`: Aktif şarkıyı sonsuz döngüye alır veya döngüyü kapatır.\n"
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
            "`w.emoji`: Sunucudaki tüm emojileri ID'leri ile birlikte listeler.\n"
            "`w.şiir`: Bilindik şairlerden rastgele efsanevi bir şiir gönderir."
        )
        embed.add_field(
            name="📖 Genel Komutlar",
            value=genel_komutlari,
            inline=False
        )

        # --- EĞLENCE & BİLGİ KOMUTLARI ---
        fun_komutlari = (
            "`w.avatar [@üye]`: Kullanıcının profil fotoğrafını yüksek kalitede gösterir.\n"
            "`w.kullanıcı-bilgi [@üye]`: Üyenin hesap kuruluş ve sunucu katılım bilgilerini verir.\n"
            "`w.sunucu-bilgi`: İçinde bulunduğunuz sunucunun detaylı istatistiklerini listeler.\n"
            "`w.zar-at`: 1 ile 6 arasında rastgele bir sayı atar.\n"
            "`w.yazı-tura`: Havaya madeni para atar (Yazı/Tura).\n"
            "`w.8ball <soru>`: Sihirli 8 topuna soru sorarsınız, o cevaplar.\n"
            "`w.aşk-ölçer <@üye1> [@üye2]`: İki kişi arasındaki aşk uyumunu ölçer.\n"
            "`w.kaç-cm [@üye]`: Eğlence amaçlı ölçüm merkezini çalıştırır.\n"
            "`w.kedi`: İnternetten rastgele tatlı bir kedi fotoğrafı getirir.\n"
            "`w.köpek`: İnternetten rastgele tatlı bir köpek fotoğrafı getirir.\n"
            "`w.espri`: Bot size soğuk bir espri patlatır.\n"
            "`w.ters-yaz <metin>`: Girdiğiniz cümlenin aynaya tutulmuş halini (tersini) verir."
        )
        embed.add_field(
            name="🏋️‍♂️ Eğlence Komutları",
            value=fun_komutlari,
            inline=False
        )

        # --- MODERASYON KOMUTLARI ---
        mod_komutlari = (
            "`w.sil <miktar>`: Kanaldaki mesajları toplu olarak siler.\n"
            "`w.kick <@üye> [sebep]`: Belirtilen üyeyi sunucudan atar.\n"
            "`w.ban <@üye> [sebep]`: Belirtilen üyeyi sunucudan yasaklar.\n"
            "`w.unban <id>`: Yasaklanmış bir üyenin yasağını ID ile kaldırır.\n"
            "`w.sustur <@üye> <süre> [sebep]`: Üyeye zamanaşımı uygular (Örn: 10m, 1h).\n"
            "`w.sustur-aç <@üye>`: Üyenin zamanaşımını / susturmasını kaldırır.\n"
            "`w.kilit`: İçinde bulunulan kanalı mesaj gönderimine kapatır.\n"
            "`w.kilit-aç`: Kilitli kanalı tekrar mesaj gönderimine açar.\n"
            "`w.yavaşmod <saniye>`: Kanal için yavaş mod süresi belirler.\n"
            "`w.rol-ver <@üye> <@rol>`: Belirtilen üyeye seçilen rolü ekler.\n"
            "`w.rol-al <@üye> <@rol>`: Belirtilen üyeden seçilen rolü geri alır.\n"
            "`w.isim <@üye> <yeni_isim>`: Üyenin sunucudaki takma adını değiştirir.\n"
            "`w.uyar <@üye> <sebep>`: Üyeyi DM üzerinden uyarır ve kanala rapor sunar."
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