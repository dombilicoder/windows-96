import discord
from discord.ext import commands

class Emoji(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="emoji")
    async def emoji_listele(self, ctx: commands.Context):
        # Sunucuda emoji var mı kontrolü
        if not ctx.guild.emojis:
            return await ctx.send("❌ Bu sunucuda hiç özel emoji bulunmuyor!")

        embed = discord.Embed(
            title=f"📁 {ctx.guild.name} - Sunucu Emojileri",
            description="Sunucuda bulunan tüm özel emojiler, ID'leri ve isimleri aşağıda listelenmiştir:",
            color=discord.Color.blurple()
        )
        
        # Discord embed mesajlarında bir alan (field) en fazla 1024 karakter alabilir.
        # Çok fazla emoji varsa hata vermemesi için emojileri gruplayarak ekliyoruz.
        sayfa_metni = ""
        grup_sayisi = 1
        
        for emoji in ctx.guild.emojis:
            # Emojinin hareketli (gif) olup olmadığını kontrol edip ona göre formatlıyoruz
            emoji_gorunumu = f"<a:{emoji.name}:{emoji.id}>" if emoji.animated else f"<:{emoji.name}:{emoji.id}>"
            satir = f"{emoji_gorunumu} | `<a:{emoji.name}:{emoji.id}>` | **{emoji.name}**\n"
            
            # Eğer mevcut metin 1000 karaktere yaklaştıysa yeni bir alan (field) açıyoruz
            if len(sayfa_metni) + len(satir) > 1000:
                embed.add_field(name=f"Liste #{grup_sayisi}", value=sayfa_metni, inline=False)
                sayfa_metni = satir
                grup_sayisi += 1
            else:
                sayfa_metni += satir
                
        # Kalan son emojileri de ekliyoruz
        if sayfa_metni:
            embed.add_field(name=f"Liste #{grup_sayisi}", value=sayfa_metni, inline=False)

        # Toplam emoji sayısını embed'in altına (footer) yazalım
        embed.set_footer(text=f"Toplam Özel Emoji Sayısı: {len(ctx.guild.emojis)}")

        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Emoji(bot))