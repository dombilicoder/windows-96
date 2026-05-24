import discord
from discord.ext import commands

class Sil(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="sil", aliases=["temizle", "purge"])
    @commands.has_permissions(manage_messages=True) # Sadece Mesajları Yönet yetkisi olanlar kullanabilir
    async def sil(self, ctx: commands.Context, miktar: int):
        if miktar <= 0:
            return await ctx.send("❌ Lütfen 1 veya daha büyük bir sayı girin.", delete_after=3)
        
        if miktar > 100:
            return await ctx.send("❌ Tek seferde en fazla 100 mesaj silebilirsiniz.", delete_after=3)

        # Kullanıcının yazdığı w.sil komutunu da dahil etmek için miktar + 1 yapıyoruz
        silinen = await ctx.channel.purge(limit=miktar + 1)
        
        # Bilgilendirme mesajı gönderip 3 saniye sonra otomatik siliyoruz
        await ctx.send(f"🧹 **{len(silinen) - 1}** adet mesaj başarıyla temizlendi!", delete_after=3)

    # Hata yönetimi (Yetkisiz kullanım veya yanlış argüman girilirse çökmemesi için)
    @sil.error
    async def sil_error(self, ctx: commands.Context, error):
        if isinstance(error, commands.MissingPermissions):
            try: await ctx.message.delete()
            except: pass
            await ctx.send("❌ Bu komutu kullanmak için **Mesajları Yönet** yetkisine sahip olmalısın.", delete_after=3)
        
        elif isinstance(error, commands.MissingRequiredArgument):
            try: await ctx.message.delete()
            except: pass
            await ctx.send("❌ Lütfen silinecek mesaj miktarını belirtin! Örn: `w.sil 50`", delete_after=3)
            
        elif isinstance(error, commands.BadArgument):
            try: await ctx.message.delete()
            except: pass
            await ctx.send("❌ Lütfen geçerli bir sayı girin!", delete_after=3)

async def setup(bot):
    await bot.add_cog(Sil(bot))