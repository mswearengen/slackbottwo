import discord
from discord.ext import commands
import asyncio

import glob
import random


class soundz(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @commands.command(aliases=['sounds'], pass_context=True)
    @commands.cooldown(rate=3, per=30)
    async def soundz(self, ctx):
        wavs = glob.glob("soundz/*.wav")
        mp3s = glob.glob("soundz/*.mp3")
        all_audio = wavs + mp3s

        selected_sound = random.choice(all_audio)

        await ctx.send(file=discord.File(selected_sound))


def setup(bot):
    bot.add_cog(soundz(bot))