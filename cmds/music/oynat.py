import discord
from discord.ext import commands
import wavelink
import os

class Oynat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.sabit_kanal_id = int(os.getenv("VOICE_CHANNEL_ID", 0))

    @commands.command(name="oynat")
    async def oynat(self, ctx: commands.Context, *, arama: str):
        if not ctx.author.voice or ctx.author.voice.channel.id != self.sabit_kanal_id:
            return await ctx.send("❌ Bu komutu kullanmak için botun bulunduğu özel ses kanalına katılmalısın!")

        vc: wavelink.Player = ctx.voice_client
        if not vc:
            return await ctx.send("Bot şu an seste değil.")

        vc.metin_kanali = ctx.channel # Kanalı hafızaya alıyoruz

        tracks: wavelink.Search = await wavelink.Playable.search(arama)
        if not tracks:
            return await ctx.send("Şarkı bulunamadı.")

        track = tracks[0]
        
        # İsteyen kişiyi player nesnesine kaydediyoruz (Hafızada kalması için)
        vc.guncel_isteyen = ctx.author 
        
        await vc.queue.put_wait(track)
        
        if not vc.playing:
            await vc.play(vc.queue.get())
        else:
            await ctx.send(f"📝 Sıraya eklendi: **{track.title}**")

async def setup(bot):
    await bot.add_cog(Oynat(bot))