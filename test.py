import discord
import os
from dpyConsole import Console
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('TOKEN')

client = discord.Client()
console = Console(client)

@client.event
async def on_ready():
    print("Logged in as a bot {0.user}".format(client))
    await client.change_presence(activity=discord.Game(name="Oyun"))

@console.command()
async def hey(user: discord.User):
    print(f"Sending message to {user.name} id: = {user.id}")
    await user.send("Hello from Console")

console.start()
client.run(token)
