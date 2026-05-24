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
        if not ctx.author.voice or ctx.author.voice.channel.id != self.sabit_kanal_id:
            return

        vc: wavelink.Player = ctx.voice_client
        if not vc or not vc.playing:
            return

        if not hasattr(vc, "dongu_acik"):
            vc.dongu_acik = False

        # Durumu değiştir
        vc.dongu_acik = not vc.dongu_acik

        # Paneldeki alanı ANINDA güncelle
        if getattr(vc, "aktif_mesaj", None):
            try:
                embed = vc.aktif_mesaj.embeds[0]
                dongu_metni = "`Açık` 🔁" if vc.dongu_acik else "`Kapalı` ❌"
                
                # Hatırlatma: 0: Sanatçı, 1: Süre, 2: Ses Seviyesi, 3: Döngü
                embed.set_field_at(3, name="🔄 Döngü", value=dongu_metni, inline=True)
                
                await vc.aktif_mesaj.edit(embed=embed)
            except Exception as e:
                print(f"Döngü güncellenirken embed hatası: {e}")

        # Mesajı silerek gizli kumanda mantığını koru
        try:
            await ctx.message.delete()
        except:
            pass

async def setup(bot):
    await bot.add_cog(Dongu(bot))