import discord
from discord.ext import commands
import wavelink
import os

class Bitir(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.sabit_kanal_id = int(os.getenv("VOICE_CHANNEL_ID", 0))

    @commands.command(name="bitir", aliases=["stop", "kapat", "leave"])
    async def bitir(self, ctx: commands.Context):
        if not ctx.author.voice or ctx.author.voice.channel.id != self.sabit_kanal_id:
            return

        vc: wavelink.Player = ctx.voice_client
        if not vc:
            return

        # Döngü açıkken bitirmeyi engelleme kilidi
        if getattr(vc, "dongu_acik", False):
            try: await ctx.message.delete()
            except: pass
            return await ctx.send("❌ **Öncelikle `w.döngü` yazarak döngüyü kapatmalısın!**", delete_after=5)

        # Sırayı temizle ve şarkıyı durdur (Kanaldan asla çıkmaz!)
        vc.queue.clear()
        
        # Bu işlem otomatik olarak on_wavelink_track_end event'ini tetikleyip paneli yeşil ve 🏁 yapar
        if vc.playing:
            await vc.stop() 
                
        # Kullanıcının w.bitir komutunu sil
        try: await ctx.message.delete()
        except: pass

async def setup(bot):
    await bot.add_cog(Bitir(bot))