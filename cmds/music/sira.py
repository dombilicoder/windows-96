import discord
from discord.ext import commands
import wavelink
import os

class Sira(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.sabit_kanal_id = int(os.getenv("VOICE_CHANNEL_ID", 0))

    @commands.command(name="sıra")
    async def sira(self, ctx: commands.Context):
        # Kullanıcının botla aynı sabit kanalda olup olmadığını kontrol ediyoruz
        if not ctx.author.voice or ctx.author.voice.channel.id != self.sabit_kanal_id:
            return await ctx.send("❌ Bu komutu kullanmak için botun bulunduğu özel ses kanalına katılmalısın!")

        vc: wavelink.Player = ctx.voice_client
        if not vc or vc.queue.is_empty:
            return await ctx.send("Sırada şarkı yok.")
        
        sira_listesi = ""
        for i, track in enumerate(vc.queue, 1):
            sira_listesi += f"**{i}.** {track.title}\n"
        
        await ctx.send(f"📑 **Müzik Sırası:**\n{sira_listesi}")

async def setup(bot):
    await bot.add_cog(Sira(bot))