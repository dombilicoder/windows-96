import discord
from discord.ext import commands
import wavelink
import os

class Dur(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.sabit_kanal_id = int(os.getenv("VOICE_CHANNEL_ID", 0))

    @commands.command(name="dur")
    async def dur(self, ctx: commands.Context):
        if not ctx.author.voice or ctx.author.voice.channel.id != self.sabit_kanal_id:
            return

        vc: wavelink.Player = ctx.voice_client
        if vc and vc.playing and not vc.paused:
            await vc.pause(True)
            
        # Sohbet kirlenmesin diye kullanıcının komut mesajını siliyoruz
        try:
            await ctx.message.delete()
        except:
            pass

async def setup(bot):
    await bot.add_cog(Dur(bot))