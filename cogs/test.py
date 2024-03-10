import requests
import discord
from discord.ext import commands

class Got(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def gotQuote(self, ctx):
        response = requests.get("https://api.gameofthronesquotes.xyz/v1/random")
        gotQuote = []

        sentence = response.json()['sentence']
        speaker = response.json()['character']['name']
        house = response.json()['character']['house']['name']

        gotQuote.append(sentence)
        gotQuote.append(speaker)
        gotQuote.append(house)

        await ctx.send(f"{gotQuote[1]} of {gotQuote[2]} says '{gotQuote[0]}'")
    
    @commands.command()
    async def search(self, ctx): # searches for an image and updates the list
        await ctx.send("HI")

async def setup(bot):
    await bot.add_cog(Got(bot))