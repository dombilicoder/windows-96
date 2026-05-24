import discord
from discord.ext import commands
import wavelink
import os

class Gec(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.sabit_kanal_id = int(os.getenv("VOICE_CHANNEL_ID", 0))

    @commands.command(name="geç")
    async def gec(self, ctx: commands.Context):
        # Kullanıcının botla aynı sabit kanalda olup olmadığını kontrol ediyoruz
        if not ctx.author.voice or ctx.author.voice.channel.id != self.sabit_kanal_id:
            return await ctx.send("❌ Bu komutu kullanmak için botun bulunduğu özel ses kanalına katılmalısın!")

        vc: wavelink.Player = ctx.voice_client
        
        if not vc or not vc.playing:
            return await ctx.send("Şu anda çalan bir şarkı yok.")
        
        if vc.queue.is_empty:
            await vc.skip(force=True)
            return await ctx.send("⏭️ Şarkı geçildi ancak sırada başka şarkı olmadığı için müzik bitti.")
        
        sonraki_sarki = vc.queue[0]
        await vc.skip(force=True)
        await ctx.send(f"⏭️ Şarkı geçildi! Şimdi oynatılıyor: **{sonraki_sarki.title}**")

async def setup(bot):
    await bot.add_cog(Gec(bot))