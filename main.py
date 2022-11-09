import discord
import os
from keep_alive import keep_alive
from discord.ext import commands
prefix = "-"
bot = commands.Bot(command_prefix=prefix) # Prefix

bot.author_id = 294809456192126976 # Author Discord ID

@bot.event 
async def on_ready():  # When the bot is ready
    print(f'{bot.user} has connected to Discord! ')
    print("我登机啦！！！")
    print("\n")

@bot.event
async def on_message(ctx):
    if ctx.author.id == bot.user.id:
      return 
    print("Receive MESSAGE")  
    await bot.process_commands(ctx)
  
@bot.command()
async def hi(ctx):
  await ctx.send("hello")

extensions = [
    'cogs.cog_example',
    'cogs.display'
]

if __name__ == '__main__':  # Ensures this is the file being ran
    for extension in extensions:
        bot.load_extension(extension)  # Loades every extension.

keep_alive()  # Starts a webserver to be pinged.
token = os.environ.get("DISCORD_BOT_SECRET") 
bot.run(token)  # Starts the bot
