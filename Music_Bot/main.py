import discord
from apikeys import *
from discord.ext import commands
from music_cog import music_cog
from help_cog import help_cog


intents = discord.Intents.all()
bot = commands.Bot(command_prefix = '!', intents=intents)
bot.add_cog(music_cog(bot))
bot.add_cog(help_cog(bot))

intents.members = True
intents.messages = True




















bot.run(token_key)