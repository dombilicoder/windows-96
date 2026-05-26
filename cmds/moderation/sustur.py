import discord
from discord.ext import commands
import datetime
import re

class Sustur(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="sustur", aliases=["timeout", "mute"])
    @commands.has_permissions(moderate_members=True)
    async def sustur(self, ctx, member: discord.Member, sure: str, *, sebep="Belirtilmedi"):
        süre_match = re.match(r"(\d+)([smhd])", sure.lower())
        if not süre_match:
            return await ctx.send("❌ Geçersiz süre formatı! Örnek: `10m` (10 dk), `1h` (1 saat)", delete_after=5)
        
        miktar = int(süre_match.group(1))
        birim = süre_match.group(2)
        
        if birim == "s": delta = datetime.timedelta(seconds=miktar)
        elif birim == "m": delta = datetime.timedelta(minutes=miktar)
        elif birim == "h": delta = datetime.timedelta(hours=miktar)
        elif birim == "d": delta = datetime.timedelta(days=miktar)

        await member.timeout(delta, reason=sebep)
        embed = discord.Embed(title="🔇 Kullanıcı Susturuldu", description=f"**Susturulan:** {member.mention}\n**Süre:** {sure}\n**Yetkili:** {ctx.author.mention}\n**Sebep:** {sebep}", color=discord.Color.dark_grey())
        await ctx.send(embed=embed, delete_after=10)
        try: await ctx.message.delete()
        except: pass

async def setup(bot):
    await bot.add_cog(Sustur(bot))