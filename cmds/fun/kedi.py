import discord
from discord.ext import commands
import aiohttp

class Kedi(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="kedi", aliases=["cat"])
    async def kedi(self, ctx):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get("https://api.thecatapi.com/v1/images/search") as response:
                    data = await response.json()
                    resim_url = data[0]["url"]
                    
            embed = discord.Embed(title="🐱 Rastgele Kedi", color=discord.Color.orange())
            embed.set_image(url=resim_url)
            await ctx.send(embed=embed)
        except:
            await ctx.send("Kedi bulunamadı, API yaramazlık yapıyor olabilir! 😿")
            

async def setup(bot):
    await bot.add_cog(Kedi(bot))