import requests # lets us grab data from the API
import discord
from discord.ext import commands # allows for the usage of commands

class Person(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def generatePerson(self, ctx): # creates an alias
        personDetails = []
        response = requests.get("https://randomuser.me/api/")
        print(response.status_code) # testing to see if valid connection has been established
        print(response.json()) # testing to see if works

        # bio
        gender = response.json()['results'][0]['gender']
        firstName = response.json()['results'][0]['name']['first']
        lastName = response.json()['results'][0]['name']['last']

        # contact
        email = response.json()['results'][0]['email']
        phone = response.json()['results'][0]['cell']

        # location
        city = response.json()['results'][0]['location']['city']
        country = response.json()['results'][0]['location']['country']

        # adds to the list
        personDetails.append(gender)
        personDetails.append(firstName)
        personDetails.append(lastName)
        
        personDetails.append(email)
        personDetails.append(phone)

        personDetails.append(city)
        personDetails.append(country)

        # prints from the list
        await ctx.send("Here is your requested alias: \n")

        await ctx.send(f"Bio:\n    Name: {personDetails[1]} {personDetails[2]} \n    Gender: {personDetails[0]}")
        await ctx.send(f"Contact:\n    Email: {personDetails[3]} \n    Phone: {personDetails[4]}")
        await ctx.send(f"Location: \n    Residency: {personDetails[5]}, {personDetails[6]}")

async def setup(bot):
    await bot.add_cog(Person(bot))
