import discord
from discord.ext import commands
import asyncio

from random import randint, choice
import json
import xmltodict
from datetime import datetime
import pytz
from lxml import html
from lxml.etree import tostring

import butil
import checks

class Misc(commands.Cog):
    """Die, die, die!"""

    def __init__(self, bot):
        self.bot = bot

    async def shake8ball(self, ctx):

        with open('8ball.json') as f:
            responses = json.load(f)['responses']

        choice = randint(0, len(responses))

        msg = '{}'.format(responses[choice]['r'])

        await ctx.send(msg)

    @commands.command()
    async def classicsofgame(self, ctx):

        with open('classicsofgame.json') as f:
                data = json.load(f)

        index = randint(0, len(data['vids']))
        url = data['vids'][index]['url']

        await ctx.send(url)


def setup(bot):
    bot.add_cog(Misc(bot))