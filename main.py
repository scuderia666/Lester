import discord
import os
import random
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

client = discord.Client()
token = os.getenv('TOKEN')

@client.event
async def on_ready():
    print("Logged in as a bot {0.user}".format(client))
    await client.change_presence(activity=discord.Game(name="oyun"))

@client.event
async def on_message(message):
	username = str(message.author).split("#")[0]
	channel = str(message.channel.name)
	user_message = str(message.content)
	author = message.author
	ment = str(author.mention)

	if user_message.lower() == "amk" or user_message.lower() == "hi":
		await message.channel.send(f'{ment} Ağzını toparla evlat.')
		return

client.run(token)
