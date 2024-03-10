import discord
from discord.ext import commands
import os
import asyncio

TOKEN = "place bot token here"

intent = discord.Intents.default()
intent.message_content = True
intent.members = True

bot = commands.Bot(command_prefix = '/', intents = intent)

cog = []

for file in os.listdir('pythonDummyBot\\cogs'):
    if file.endswith('.py'):
        cog.append("cogs." + file[:-3])

async def load():
    for c in cog:
        await bot.load_extension(c)

# msg on bot start
@bot.event
async def on_ready():
    print(f"{bot.user} is now active")

# msg when person joins the server
@bot.event
async def on_member_join(member):
    channel = bot.get_channel("place channel id here")
    await channel.send(f"Welcome to the server {member.mention}!")

# msg when person leaves the server
@bot.event
async def on_member_remove(member):
    channel = bot.get_channel("place channel id here")
    await channel.send(f"We're so sad to see you go {member.mention}!")

# shuts the bot down
@bot.command()
async def shutdown(ctx):
    await exit()

async def main():
    async with bot:
        await load()
        await bot.start(TOKEN)

asyncio.run(main())

