import discord
from discord.ext import commands
import wavelink

class Sonsuz(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        # Discord linki bir süre sonra patlarsa, buraya doğrudan bir YouTube linki yapıştırabilirsin.
        # Örn: "https://www.youtube.com/watch?v=J_36x1_LKgg"
        self.muzik_linki = "https://cdn.discordapp.com/attachments/1509361095905644554/1509361124989210707/gnosienneno1.mp3?ex=6a18e596&is=6a179416&hm=8473c2c5819b1cabc0608ff7cbdbad7f7224617356a9c2938e00d4a27a9a844a&"

    @commands.command(name="sonsuz", hidden=True)
    @commands.has_permissions(manage_messages=True)
    async def sonsuz(self, ctx):
        if not ctx.author.voice:
            return await ctx.send("❌ Önce bir ses kanalına katılmalısın!")

        # Bota bağlan veya zaten bağlıysa mevcut player'ı al
        if not ctx.voice_client:
            vc: wavelink.Player = await ctx.author.voice.channel.connect(cls=wavelink.Player)
        else:
            vc: wavelink.Player = ctx.voice_client

        try:
            # Wavelink ile URL üzerinden şarkıyı aratıyoruz
            sarkilar = await wavelink.Playable.search(self.muzik_linki)
            if not sarkilar:
                return await ctx.send("❌ Link okunamadı! (Discord linkinin süresi dolmuş olabilir).")
            
            # Wavelink search genelde URL'ler için liste döndürür, ilkini alıyoruz
            sarki = sarkilar[0] if isinstance(sarkilar, list) else sarkilar
            
            # Zombi bot olmasını engelleyen döngü modumuzu açıyoruz
            vc.dongu_acik = True
            
            # Eğer daha önceden başka bir şarkı çalıyorsa durdur
            if vc.is_playing():
                await vc.stop()
                
            await vc.play(sarki)
            await ctx.send("♾️ **Sonsuz Mod Aktif:** Gnossienne No.1 döngüye alındı. Kapatmak için `w.sonsuz-iptal` yazın.")
            
        except Exception as e:
            await ctx.send(f"❌ Bir hata oluştu: {e}")

    @commands.command(name="sonsuz-iptal", hidden=True)
    @commands.has_permissions(manage_messages=True)
    async def sonsuz_iptal(self, ctx):
        if not ctx.voice_client:
            return await ctx.send("❌ Bot zaten seste değil hacı.")
        
        vc: wavelink.Player = ctx.voice_client
        vc.dongu_acik = False  # Döngüyü kır
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