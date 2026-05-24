import discord
from discord.ext import commands
import wavelink
import os

class Ses(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.sabit_kanal_id = int(os.getenv("VOICE_CHANNEL_ID", 0))

    @commands.command(name="ses", aliases=["volume", "vol"])
    async def ses(self, ctx: commands.Context, miktar: int):
        # Sabit ses kanalında değilse komutu görmezden geliyoruz
        if not ctx.author.voice or ctx.author.voice.channel.id != self.sabit_kanal_id:
            return

        vc: wavelink.Player = ctx.voice_client
        if not vc or not vc.playing:
            return

        # Yardım menüsündeki gibi ses seviyesini 0 ile 500 arasında sınırlandırıyoruz
        miktar = max(0, min(miktar, 500))
        
        # Botun ses seviyesini ayarlıyoruz
        await vc.set_volume(miktar)
        
        # 5 saniyelik döngüyü beklemeden embed üzerindeki alanı ANINDA güncelliyoruz
        if getattr(vc, "aktif_mesaj", None):
            try:
                embed = vc.aktif_mesaj.embeds[0]
                
                # Hatırlatma: Alan sıralaması -> 0: Sanatçı, 1: Süre, 2: Ses Seviyesi
                embed.set_field_at(2, name="🔊 Ses Seviyesi", value=f"`%{miktar}`", inline=True)
                
                await vc.aktif_mesaj.edit(embed=embed)
            except Exception as e:
                print(f"Ses güncellenirken embed hatası: {e}")

        # Sohbet temizliği için kullanıcının w.ses mesajını siliyoruz
        try:
            await ctx.message.delete()
        except:
            pass

async def setup(bot):
    await bot.add_cog(Ses(bot))