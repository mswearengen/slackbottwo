import discord
from discord.ext import commands
import asyncio

import glob
import random


class petz(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @commands.command(aliases=['pets'], pass_context=True)
    @commands.cooldown(rate=3, per=30)
    async def petz(self, ctx):
        jpgs = glob.glob("petz/*.jpg")
        pngs = glob.glob("petz/*.png")
        all_imgs = jpgs + pngs

        selected_img = random.choice(all_imgs)

        await ctx.send(file=discord.File(selected_img))


def setup(bot):
    bot.add_cog(petz(bot))