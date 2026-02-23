import discord
from discord.ext import commands
from model import *

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for a in ctx.message.attachments:
            file_name = a.filename
            file_path = f"./images/{file_name}"

            await a.save(file_path)
            await ctx.send(getclass(file_path))

    else:
        await ctx.send("image not found!")


bot.run("token")  # Reemplaza "token" con tu token real de Discord