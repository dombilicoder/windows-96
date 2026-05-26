import discord
from discord.ext import commands

class Uyar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="uyar", aliases=["warn"])
    @commands.has_permissions(kick_members=True)
    async def uyar(self, ctx, member: discord.Member, *, sebep: str):
        embed = discord.Embed(title="⚠️ Uyarıldınız", description=f"**{ctx.guild.name}** sunucusunda bir yetkili tarafından uyarıldınız.\n**Sebep:** {sebep}", color=discord.Color.yellow())
        try:
            await member.send(embed=embed)
            dm_durum = "DM Yoluyla İletildi ✅"
        except:
            dm_durum = "DM Kapalı Olduğu İçin İletilemedi ❌"

        log_embed = discord.Embed(
            title="⚠️ Kullanıcı Uyarıldı", 
            description=f"**Uyarılan Kullanıcı:** {member.mention}\n**Yetkili:** {ctx.author.mention}\n**Sebep:** {sebep}\n**Durum:** {dm_durum}", 
            color=discord.Color.yellow()
        )
        
        # --- HATA BURADAYDI: log_embed'ın başına embed= ekledik ---
        await ctx.send(embed=log_embed, delete_after=15)
        
        try: await ctx.message.delete()
        except: pass

async def setup(bot):
    await bot.add_cog(Uyar(bot))