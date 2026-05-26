import discord
from discord.ext import commands

class KullaniciBilgi(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="kullanıcı-bilgi", aliases=["kullanici-bilgi", "userinfo"])
    async def kullanici_bilgi(self, ctx, member: discord.Member = None):
        member = member or ctx.author
        roles = [role.mention for role in member.roles[1:]]
        roles_text = " ".join(roles) if roles else "Rolü Yok"
        
        embed = discord.Embed(title=f"👤 Kullanıcı Bilgisi: {member.name}", color=member.color)
        embed.set_thumbnail(url=member.display_avatar.url)
        embed.add_field(name="ID", value=f"`{member.id}`", inline=True)
        embed.add_field(name="Takma Ad", value=f"`{member.display_name}`", inline=True)
        embed.add_field(name="Hesap Kuruluş", value=f"<t:{int(member.created_at.timestamp())}:D>", inline=True)
        embed.add_field(name="Sunucuya Katılım", value=f"<t:{int(member.joined_at.timestamp())}:D>", inline=True)
        embed.add_field(name=f"Roller [{len(roles)}]", value=roles_text, inline=False)
        
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(KullaniciBilgi(bot))