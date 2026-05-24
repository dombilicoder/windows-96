import discord
from discord.ext import commands
import wavelink
import os

class Bitir(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.sabit_kanal_id = int(os.getenv("VOICE_CHANNEL_ID", 0))

    @commands.command(name="bitir")
    async def bitir(self, ctx: commands.Context):
        if not ctx.author.voice or ctx.author.voice.channel.id != self.sabit_kanal_id:
            return await ctx.send("❌ Bunu yapmak için botun bulunduğu ses kanalında olmalısın.")

        vc: wavelink.Player = ctx.voice_client
        if vc:
            vc.queue.clear()
            await vc.skip(force=True)
            vc.aktif_mesaj = None
            await ctx.send("🛑 Müzik tamamen bitirildi ve sıra temizlendi.")
        else:
            await ctx.send("Zaten aktif bir müzik yok.")

async def setup(bot):
    await bot.add_cog(Bitir(bot))