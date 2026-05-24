import discord
from discord.ext import commands
import wavelink
import os

class Dongu(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.sabit_kanal_id = int(os.getenv("VOICE_CHANNEL_ID", 0))

    @commands.command(name="döngü", aliases=["dongu", "loop"])
    async def dongu(self, ctx: commands.Context):
        # Sabit ses kanalında değilse komutu görmezden geliyoruz
        if not ctx.author.voice or ctx.author.voice.channel.id != self.sabit_kanal_id:
            return

        vc: wavelink.Player = ctx.voice_client
        if not vc or not vc.playing:
            return

        # Player nesnesine daha önce eklenmediyse döngü durumunu oluşturuyoruz
        if not hasattr(vc, "dongu_acik"):
            vc.dongu_acik = False

        # Durumu tersine çeviriyoruz (Açıksa kapat, kapalıysa aç)
        vc.dongu_acik = not vc.dongu_acik

        # Canlı paneli anında güncelle (Döngüyü bekleme)
        if getattr(vc, "aktif_mesaj", None):
            try:
                embed = vc.aktif_mesaj.embeds[0]
                durum_metni = "Açık 🔁" if vc.dongu_acik else "Kapalı ❌"
                
                # Eğer yardım menüsündeki gibi footer'a veya ekstra alana eklemek istersen 
                # Burada da anlık tazeleyebiliriz. Ancak embed_guncelleyici zaten 3 saniyede bir basacak.
                # Açıklama (description) kısmındaki emojiyi anında değiştirmek için tetikleyelim:
                position = vc.position
                length = vc.current.length if vc.current else 0
                total_bars = 15
                percentage = position / length if length > 0 else 0
                filled = max(0, min(total_bars, int(percentage * total_bars)))
                bar_list = ["-"] * total_bars
                bar_list[min(filled, total_bars-1)] = "•"
                
                p_min, p_sec = divmod(int(position / 1000), 60)
                l_min, l_sec = divmod(int(length / 1000), 60)
                
                # Döngü açıksa emoji 🔁 olacak
                emoji = "🔁" if vc.dongu_acik else ("⏸️" if vc.paused else "🎵")
                embed.description = f"{emoji} `{''.join(bar_list)}` `{p_min:02d}:{p_sec:02d}/{l_min:02d}:{l_sec:02d}`"
                
                await vc.aktif_mesaj.edit(embed=embed)
            except:
                pass

        # Sohbet temizliği için w.döngü mesajını siliyoruz
        try:
            await ctx.message.delete()
        except:
            pass

async def setup(bot):
    await bot.add_cog(Dongu(bot))