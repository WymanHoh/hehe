import discord
from discord.ext import commands

class Display(commands.Cog):

  def __init__(self,bot):
    self.bot=bot

  #event
  @commands.Cog.listener()
  async def on_ready(self):
    print("I am functionable.")

  #commands
  @commands.command()
  async def ping(self,ctx):
    await ctx.send("ponggg!")

  @commands.command()
  async def test(self,ctx):
    await ctx.send("bakarayo")

    
def setup(bot):
  bot.add_cog(Display(bot))