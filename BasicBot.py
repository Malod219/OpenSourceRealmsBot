# These are the dependecies. The bot depends on these to function, hence the name. Please do not change these unless your adding to them, because they can break the bot.
import discord
import csv
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform
from datetime import datetime

#Credentials, Tokens etc
import credentials

# Modify command prefix
bot = Bot(description="PiPy Bot", command_prefix=">", pm_help = False)

#Prints generic bot information to consol
@bot.event
async def on_ready():
        print('Logged in as '+bot.user.name+' (ID:'+bot.user.id+') | Connected to '+str(len(bot.servers))+' servers | Connected to '+str(len(set(bot.get_all_members())))+' users')
        print('Current Discord.py Version: {} | Current Python Version: {}'.format(discord.__version__, platform.python_version()))
        print('Invitation to bring this to the server {}:'.format(bot.user.name))
        print('https://discordapp.com/oauth2/authorize?bot_id={}&scope=bot&permissions=8'.format(bot.user.id))
        print("Start time:" + datetime.now().strftime("%Y-%m-%d %H:%M"))
        bot.day=datetime.now().strftime("%Y-%m-%d")
        print(bot.day)
        return await bot.change_presence(game=discord.Game(name='DungeonRealms'))

        
bot.remove_command('help')
@bot.command(pass_context=True)
async def help(ctx):
        embed = discord.Embed(title="Help commands", description="Help Commands are:", color=0xeee657)
        embed.add_field(name=">admin help", value="Lists commands for admin", inline=False)
        embed.add_field(name=">mc help", value="Lists commands for mc", inline=False)
        embed.add_field(name=">misc help", value="Some Miscellaneous Commands.", inline=False)
        embed.add_field(name=">rss help", value="Lists commands for rss commands", inline=False)
        embed.add_field(name=">server help", value="Lists commands for server commands", inline=False)
        embed.add_field(name=">info", value="More information on the bot.", inline=False)
        embed.add_field(name=">server info", value="More information on the bot.", inline=False)
        await bot.send_message(ctx.message.author, embed=embed)


@bot.command(pass_context=True)
async def info(ctx):
        embed = discord.Embed(title="General Information", description="General Information on OpenRealms project.", color=0xeee657)
        embed.add_field(name="Who it is developed by:", value="ODST", inline=False)
        embed.add_field(name="Am I paid/volunteer developer for DungeonRealms", value="No.", inline=False)
        embed.add_field(name="Why did you make this?", value="Practice, fun. What's not to love about bots. Also CS practice for Uni next year.", inline=False)
        embed.add_field(name="When is it updated:", value="Every week on Friday for the live bot", inline=False)
        embed.add_field(name="How is it hosted:", value="On a Raspberry Pi at home like the rest of my bots", inline=False)
        embed.add_field(name="Can I develop this with you?", value="No need to ask if you can. Contribute to the source code below!", inline=False)
        embed.add_field(name="Bugs/problems", value="https://github.com/Malod219/OpenSourceRealmsBot/issues", inline=False)
        embed.add_field(name="Source Code", value="https://github.com/Malod219/OpenSourceRealmsBot", inline=False)
        embed.add_field(name="Contact Me", value="Discord@ODST#7648 Skype@perfectodst", inline=False)
        await bot.send_message(ctx.message.author, embed=embed)

@bot.command(pass_context=True,aliases=['server info'])
async def serverinfo(ctx):
        embed = discord.Embed(title="Server Info", description="Server Information", color=0xeee657)
        embed.add_field(name="DungeonRealms IP", value="play.dungeonrealms.net", inline=False)
        embed.add_field(name="DungeonRealms Map", value="http://minemap.net/DungeonRealms/", inline=False)
        embed.add_field(name="DungeonRealms Wikia", value="http://dungeonrealms.wikia.com/wiki/Main_Page", inline=False)
        embed.add_field(name="DungeonRealms Discord", value="https://discordapp.com/invite/GcD9nbZ", inline=False)
        embed.add_field(name="DungeonRealms Github", value="https://github.com/DungeonRealms", inline=False)
        embed.add_field(name="DungeonRealms Shop", value="https://www.dungeonrealms.net/shop", inline=False)
        embed.add_field(name="DungeonRealms Reddit", value="https://www.reddit.com/r/dungeonrealms/", inline=False)
        embed.add_field(name="DungeonRealms Twitter", value="https://twitter.com/DungeonRealms", inline=False)
        await bot.send_message(ctx.message.author, embed=embed)

        
initial_extensions=[
        'Namemc',
        'Administration',
        'Misc',
        'RSS',
        'Server'
        ]
channellist=[]


if __name__=='__main__':
        for extension in initial_extensions:
                bot.load_extension(extension)
        
bot.run(credentials.bot_token)
