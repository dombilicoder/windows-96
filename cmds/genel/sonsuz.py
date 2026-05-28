import discord
from discord.ext import commands
import wavelink
import os

class Sonsuz(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="sonsuz", hidden=True)
    @commands.has_permissions(manage_messages=True)
    async def sonsuz(self, ctx):
        if not ctx.author.voice:
            return await ctx.send("❌ Önce bir ses kanalına katılmalısın!")

        if not ctx.voice_client:
            vc: wavelink.Player = await ctx.author.voice.channel.connect(cls=wavelink.Player)
        else:
            vc: wavelink.Player = ctx.voice_client

        # Botun ana klasöründeki gnosienneno1.mp3 dosyasını hedef alıyoruz
        dosya_yolu = os.path.abspath("gnosienneno1.mp3")
        
        if not os.path.exists(dosya_yolu):
            return await ctx.send("❌ `gnosienneno1.mp3` dosyası Render sunucusunda (ana klasörde) bulunamadı! Lütfen dosyayı git ile pushladığından emin ol.")

        try:
            # Wavelink'e yerel dosyanın tam yolunu veriyoruz
            sarkilar = await wavelink.Playable.search(dosya_yolu)
            if not sarkilar:
                return await ctx.send("❌ Dosya Render üzerinde Lavalink tarafından okunamadı.")
            
            sarki = sarkilar[0]
            
            vc.dongu_acik = True
            
            # HATA VEREN KISIM BURASIYDI, "playing" OLARAK DÜZELTİLDİ:
            if vc.playing:
                await vc.stop()
                
            await vc.play(sarki)
            await ctx.send("♾️ **Sonsuz Mod Aktif:** Render üzerindeki `gnosienneno1.mp3` döngüye alındı. Kapatmak için `w.sonsuz-iptal` yazın.")
            
        except Exception as e:
            await ctx.send(f"❌ Bir hata oluştu: {e}")

    @commands.command(name="sonsuz-iptal", hidden=True)
    @commands.has_permissions(manage_messages=True)
    async def sonsuz_iptal(self, ctx):
        if not ctx.voice_client:
            return await ctx.send("❌ Bot zaten seste değil hacı.")
        
        vc: wavelink.Player = ctx.voice_client
        vc.dongu_acik = False
        
        # Olası bir hatayı önlemek için burayı da playing olarak kontrol edelim
        if vc.playing:
            await vc.stop()
            
        await vc.disconnect()
        
        await ctx.send("🛑 **Sonsuz Mod Kapatıldı:** Müzik bitirildi ve kanaldan çıkıldı.")

    @sonsuz.error
    @sonsuz_iptal.error
    async def sonsuz_hata(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("❌ Bu komut gizlidir ve sadece **Moderatörler** kullanabilir!")

async def setup(bot):
    await bot.add_cog(Sonsuz(bot))