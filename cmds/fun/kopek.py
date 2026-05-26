import discord
from discord.ext import commands
import aiohttp

class Kopek(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="köpek", aliases=["kopek", "dog"])
    async def kopek(self, ctx):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get("https://dog.ceo/api/breeds/image/random") as response:
                    data = await response.json()
                    resim_url = data["message"]
                    
            embed = discord.Embed(title="🐶 Rastgele Köpek", color=discord.Color.blurple())
            embed.set_image(url=resim_url)
            await ctx.send(embed=embed)
        except:
            await ctx.send("Köpek bulunamadı, API mamasını yiyor! 🦴")
            

async def setup(bot):
    await bot.add_cog(Kopek(bot))