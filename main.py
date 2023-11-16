import discord
import os
from dotenv import load_dotenv

import subprocess

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bot = discord.Bot(intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

@bot.slash_command(name = "hello", description = "Say hello to the bot")
async def hello(ctx):
    await ctx.respond("Hey!")

@bot.slash_command(name = "weather", description = "Get weather information")
async def weather(ctx, location: discord.Option(description='Location')):
    await ctx.defer()

    weather_information = subprocess.run(['curl', '-s', f'https://wttr.in/{location}?format=3'], capture_output=True, text=True)
    await ctx.respond(weather_information.stdout)

bot.run(os.getenv('TOKEN'))
