import discord
from discord.ext import commands
import wavelink
import os

class Sar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.sabit_kanal_id = int(os.getenv("VOICE_CHANNEL_ID", 0))

    @commands.command(name="sar")
    async def sar(self, ctx: commands.Context, saniye: int):
        if not ctx.author.voice or ctx.author.voice.channel.id != self.sabit_kanal_id:
            return

        vc: wavelink.Player = ctx.voice_client
        if not vc or not vc.playing:
            return

        # Wavelink'te süreler milisaniye (ms) cinsindendir.
        # Mevcut sürenin üzerine girilen saniyeyi ekliyoruz.
        yeni_pozisyon = vc.position + (saniye * 1000)
        
        # Eğer girilen saniye şarkının toplam süresini aşıyorsa veya eksi girilip 0'ın altına düşüyorsa
        yeni_pozisyon = max(0, min(yeni_pozisyon, vc.current.length - 1000))

        await vc.seek(yeni_pozisyon)
        
        try:
            await ctx.message.delete()
        except:
            pass

async def setup(bot):
    await bot.add_cog(Sar(bot))