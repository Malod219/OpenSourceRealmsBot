import discord
import asyncio
from discord.ext import commands
import aiohttp
import async_timeout
from bs4 import BeautifulSoup
import json
from mcstatus import MinecraftServer
import random
server = MinecraftServer.lookup("play.dungeonrealms.net")

#bot Location CommandParent
class misc:
    def __init__(self,bot):
        self.bot = bot
    @commands.group(pass_context=True)
    async def misc(self,ctx):
        if ctx.invoked_subcommand is None:
            await self.bot.say('No command entered.')


    @misc.command(pass_context=True)
    async def help(self,ctx):
        embed = discord.Embed(title="Misc Commands", description="Misc Commands are:", color=0xeee657)

        embed.add_field(name=">misc roll [number]", value="Rolls a number between 0 and number selected.", inline=False)
        await self.bot.send_message(ctx.message.author, embed=embed)

    @misc.command(pass_context=True)
    async def roll(self,ctx,*args):
        try:
            number=int(args[0])
            outputNum=random.randint(0,number)
            await self.bot.send_message(ctx.message.channel,"You rolled : "+str(outputNum)+"/"+str(number))
        except:
            await self.bot.send_message(ctx.message.channel,"You didn't input a number")

                    
def setup(bot):
    bot.add_cog(misc(bot))
