import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Connecté en tant que {bot.user}")

@bot.command()
async def charal(ctx):
    await ctx.send("hmmm charal")

TOKEN = os.environ.get("DISCORD_TOKEN")
bot.run(MTQ4MTcxMTk0MjAyMzI1NDA1Ng.Gy99Ja.wUHIFQ3OFcAeUxnmqaP9LYXRxcq4b1JK8amsdw)