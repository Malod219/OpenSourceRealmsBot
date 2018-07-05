import discord
import asyncio
from discord.ext import commands
import aiohttp
import async_timeout
from bs4 import BeautifulSoup
import json
from mcstatus import MinecraftServer
import random

#bot Location CommandParent
class server:
    def __init__(self,bot):
        self.bot = bot
    @commands.group(pass_context=True)
    async def server(self,ctx):
        if ctx.invoked_subcommand is None:
            await self.bot.say('No command entered.')


    @server.command(pass_context=True)
    async def help(self,ctx):
        embed = discord.Embed(title="Server Commands", description="Misc Commands are:", color=0xeee657)
        embed.add_field(name=">server ip", value="Gives ip", inline=False)
        embed.add_field(name=">server map", value="Gives map", inline=False)
        embed.add_field(name=">server forums", value="Gives forums link", inline=False)
        embed.add_field(name=">server playercount", value="Gives a list of servers and the number online", inline=False)
        await self.bot.send_message(ctx.message.author, embed=embed)

    @server.command(pass_context=True)
    async def playercount(self,ctx):
        server = MinecraftServer.lookup("play.dungeonrealms.net")
        status =  server.status()
        await self.bot.send_message(ctx.message.channel,"Players online : "+str(status.players.online))

    @server.command(pass_context=True)
    async def ip(self,ctx):
        await self.bot.send_message(ctx.message.channel,"Server IP : play.dungeonrealms.net")

    @server.command(pass_context=True)
    async def forums(self,ctx):
        await self.bot.send_message(ctx.message.channel,"Server forums : https://www.dungeonrealms.net/forum")

    @server.command(pass_context=True)
    async def map(self,ctx):
        await self.bot.send_message(ctx.message.channel,"Server map : http://minemap.net/DungeonRealms/")

    @server.command(pass_context=True)
    async def info(self,ctx):
        embed = discord.Embed(title="Server Info", description="Server Information", color=0xeee657)
        embed.add_field(name="DungeonRealms IP", value="play.dungeonrealms.net", inline=False)
        embed.add_field(name="DungeonRealms Map", value="http://minemap.net/DungeonRealms/", inline=False)
        embed.add_field(name="DungeonRealms Wikia", value="http://dungeonrealms.wikia.com/wiki/Main_Page", inline=False)
        embed.add_field(name="DungeonRealms Discord", value="https://discordapp.com/invite/GcD9nbZ", inline=False)
        embed.add_field(name="DungeonRealms Github", value="https://github.com/DungeonRealms", inline=False)
        embed.add_field(name="DungeonRealms Shop", value="https://www.dungeonrealms.net/shop", inline=False)
        embed.add_field(name="DungeonRealms Reddit", value="https://www.reddit.com/r/dungeonrealms/", inline=False)
        embed.add_field(name="DungeonRealms Twitter", value="https://twitter.com/DungeonRealms", inline=False)
        await self.bot.send_message(ctx.message.author, embed=embed)

                    
def setup(bot):
    bot.add_cog(server(bot))
