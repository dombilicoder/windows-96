import discord
from discord.ext import commands
import wavelink
import os

class Devam(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.sabit_kanal_id = int(os.getenv("VOICE_CHANNEL_ID", 0))

    @commands.command(name="devam")
    async def devam(self, ctx: commands.Context):
        if not ctx.author.voice or ctx.author.voice.channel.id != self.sabit_kanal_id:
            return

        vc: wavelink.Player = ctx.voice_client
        if vc and vc.paused:
            await vc.pause(False)
            
        try:
            await ctx.message.delete()
        except:
            pass

async def setup(bot):
    await bot.add_cog(Devam(bot))