import discord
from discord.ext import commands
import random

class Espri(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="espri", aliases=["joke"])
    async def espri(self, ctx):
        espriler = [
            "Röntgen Filmi çektirdik, yakında sinemalarda.",
            "Yıkanan Ton’a ne denir? Washington!",
            "Kediler havaalanına neden gidemez? Çünkü orada pist var.",
            "Adamın biri gülmüş, saksıya koymuşlar.",
            "Ben kahve içiyorum, Nurgül Yeşilçay.",
            "En çok e-mail atan kuş hangisidir? Bay-kuş!",
            "Fransızların nesi eksiktir? 'Fran'ları, çünkü hepsi 'Sız'.",
            "Siviller hangi dili konuşur? Sivilce."
        ]
        
        embed = discord.Embed(title="🤡 Günün Esprisi", description=random.choice(espriler), color=discord.Color.yellow())
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Espri(bot))