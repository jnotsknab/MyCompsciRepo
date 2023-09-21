###import discord library
import discord
### import commands for bot
from discord.ext import commands

from apikeys import *
### initialize the bot
intents = discord.Intents.all()
intents.messages = True
intents.members = True

client = commands.Bot(command_prefix = '!', intents = intents)

###bot listens for message starting with ! mark to call the bot and execute whichever function was called

@client.event
async def on_ready():
    print('Bot is now ready to receive commands')
    print('------------------------------------')


@client.command()
async def hello(ctx):
    await ctx.send("This is a test bot")


@client.command()
@commands.is_owner()
async def shutdown(ctx):
    exit()

# defining an event that detects when user joins the server (action) and runs a piece of code that displays a message in server
@client.event
async def on_member_join(member):
    channel = client.get_channel(1056377505147277335)
    await channel.send('HI BOAHHH')
    


@client.command()
async def goodbye(ctx):
    await ctx.send("Bot go bye bye now!")

client.run(token)

###need to tell this code which application to link up to within the discord dev portal
##put token in the run parameter
##token links bot to application, very important dont share it, if someone else has token they have control of bot and server, thus personal info


###discord bot yt vid #2 events and commands
##good practice to have seperate folder for all apikeys/variables (application programming interface) basically allows the code i write to interact with various applications

##event = when an event detects a certain action it will run a certain piece of code (when detects certain something it will do certain something)





