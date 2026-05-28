import discord
from discord.ext import commands
import wavelink

class Sonsuz(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        # Patlama riski olmayan, klasikleşmiş YouTube linkini gömüyoruz
        self.muzik_linki = "https://www.youtube.com/watch?v=J_36x1_LKgg"

    @commands.command(name="sonsuz", hidden=True)
    @commands.has_permissions(manage_messages=True)
    async def sonsuz(self, ctx):
        if not ctx.author.voice:
            return await ctx.send("❌ Önce bir ses kanalına katılmalısın!")

        if not ctx.voice_client:
            vc: wavelink.Player = await ctx.author.voice.channel.connect(cls=wavelink.Player)
        else:
            vc: wavelink.Player = ctx.voice_client

        try:
            # Artık sahte local dosyalarla uğraşmıyoruz, direkt YouTube URL'sini çekiyoruz
            sarkilar = await wavelink.Playable.search(self.muzik_linki)
            if not sarkilar:
                return await ctx.send("❌ Şarkı YouTube üzerinden çekilemedi.")
            
            sarki = sarkilar[0] if isinstance(sarkilar, list) else sarkilar
            
            vc.dongu_acik = True
            
            if vc.playing:
                await vc.stop()
                
            await vc.play(sarki)
            await ctx.send("♾️ **Sonsuz Mod Aktif:** Gnossienne No.1 (YouTube üzerinden) döngüye alındı. Kapatmak için `w.sonsuz-iptal` yazın.")
            
        except Exception as e:
            await ctx.send(f"❌ Bir hata oluştu: {e}")

    @commands.command(name="sonsuz-iptal", hidden=True)
    @commands.has_permissions(manage_messages=True)
    async def sonsuz_iptal(self, ctx):
        if not ctx.voice_client:
            return await ctx.send("❌ Bot zaten seste değil hacı.")
        
        vc: wavelink.Player = ctx.voice_client
        vc.dongu_acik = False
        
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