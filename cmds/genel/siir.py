import discord
from discord.ext import commands
import random
import os

class Siir(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.dosya_yolu = "siirler.txt"

    def load_siirler(self):
        if not os.path.exists(self.dosya_yolu):
            return []
        
        try:
            with open(self.dosya_yolu, "r", encoding="utf-8") as f:
                content = f.read()
        except:
            return []
            
        # Şiirleri === ayıracına göre listeye bölüyoruz
        ham_siirler = content.split("===")
        arsiv = []
        
        for ham in ham_siirler:
            if not ham.strip():
                continue
                
            satirlar = ham.strip().split("\n")
            yazar = "Bilinmiyor"
            baslik = "Başlıksız"
            metin_satirlari = []
            
            for satir in satirlar:
                # Büyük/küçük harf duyarlılığını önlemek için kontrol
                if satir.upper().startswith("YAZAR:"):
                    yazar = satir[6:].strip()
                elif satir.upper().startswith("BAŞLIK:"):
                    baslik = satir[7:].strip()
                else:
                    metin_satirlari.append(satir)
                    
            metin_tam = "\n".join(metin_satirlari).strip()
            if metin_tam:
                arsiv.append({
                    "yazar": yazar,
                    "baslik": baslik,
                    "metin": metin_tam
                })
        return arsiv

    @commands.command(name="şiir", aliases=["siir", "poem"])
    async def siir(self, ctx):
        arsiv = self.load_siirler()
        
        if not arsiv:
            await ctx.send("❌ Şiir arşivi boş veya `siirler.txt` dosyası bulunamadı!")
            return

        secilen_siir = random.choice(arsiv)
        
        embed = discord.Embed(
            title=f"📜 {secilen_siir['baslik']}", 
            description=secilen_siir['metin'], 
            color=discord.Color.dark_red()
        )
        embed.set_footer(text=f"✒️ Şair: {secilen_siir['yazar']} | Windows 96 Edebiyat Kulübü")
        
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Siir(bot))