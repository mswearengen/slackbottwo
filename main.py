import discord
import os
from discord.ext import commands
import asyncio

import re
import json

import logging

logging.basicConfig(level=logging.INFO)

extensions = [
    'misc',
    'mfw',
    'petz',
    'soundz'
]

token = os.getenv('BOT_KEY')
bot = commands.Bot(command_prefix=commands.when_mentioned_or())

@bot.event
async def on_ready():
    print("{} connected".format(bot.user.name))


@bot.event
async def on_message(message):

    ctx = await bot.get_context(message)

    message.content = message.content.replace('  ', ' ')

    message.content = message.content.lower()

    mentioned = False
    for m in message.mentions:
        if m.name == bot.user.name and m.id == bot.user.id:
            mentioned = True

    if mentioned:
        mentioned = False
        if message.content.endswith('?'):
            await bot.get_cog('Misc').shake8ball(ctx)
        else:
            with open("tags.json") as f:
                tags = json.load(f)

            try:
                out = tags[message.content.split()[1]]
                await ctx.send(message.out)
            except:
                    pass

    await bot.process_commands(message)


for extension in extensions:
    try:
        bot.load_extension(extension)
    except Exception as e:
        print('Failed to load extension {}\n{}: {}'.format(
            extension, type(e).__name__, e))
bot.run(token)
