import discord
import os
import random
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

client = discord.Client()
token = os.getenv('TOKEN')

arr = {}

@client.event
async def on_ready():
    print("Logged in as a bot {0.user}".format(client))
    await client.change_presence(activity=discord.Game(name="Oyun"))

def add_warn(username):
	if username not in arr:
		arr[username] = 0
	arr[username] = arr[username] + 1

async def dm(ctx):
    user=await client.get_user_info("User's ID here")
    await client.send_message(user, "Your message goes here")

async def send_channel_entry():
    channel = client.get_channel(channel_entry)
    await channel.send(msg_entry)

@client.event
async def on_message(message):
	author = message.author
	author_name = str(author)
	username = author_name.split("#")[0]
	channel = message.channel
	if channel is not None:
		print(channel.id)
	user_message = str(message.content)
	ment = str(author.mention)

	print("{}: {}".format(username, user_message))

	if user_message[:1] == "!":
		command = user_message[1:]

		if command == "ping":
			await message.channel.send(f"pong")

	if user_message[:1] == "&":
		msg = user_message[1:]
		await client.get_channel(int(msg.split(':',1)[0])).send(msg.split(':',1)[1])

	if user_message[:1] == "%":
		msgg = user_message[1:]
		msg = msgg.split('!')[1]
		print(msgg.split('!')[0])
		namee = msg.split(':')[0]
		nick = namee.split('#')[0]
		idd = namee.split('#')[1]
		guild = client.get_guild(int(msgg.split('!')[0]))
		user = discord.utils.get(guild.members, name=nick, discriminator=idd)
		await client.send_message(user, msg.split(':')[1])

	if client.user.mentioned_in(message):
		add_warn(username)
		if arr[username] > 1:
			await message.channel.send(f"{ment} Bu son uyarıydı.")
			await message.channel.send(f"!mute {ment}")
		else:
			await message.channel.send(f"{ment} Adminleri pinglememelisin evlat.")

	if "amk" in user_message.lower() or "aq" in user_message.lower():
		await message.channel.send(f'{ment} Ağzını toparla evlat.')
		add_warn(username)

client.run(token)
