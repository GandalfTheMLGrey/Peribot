import discord
from discord.ext import commands
import random
from random import choice
from datetime import datetime
import re

class Hiatus:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='hiatus',
                    description="How long has this Hiatus been going on for?",
                    breif="The hiatus is cold and long",
                    pass_context=False)
    async def hiatus(self):
        """
        Will return the number of days since the last episode of SVTFOE. The nexus of the hiatus...
        :return: Preformated Message with calculated days
        """
        date_of_last_episode = datetime.strptime('Apr 7 2018 01:00AM',
                                                 '%b %d %Y %I:%M%p')  # Set from config
        days = re.search('\d{1,3}\s', str(datetime.now() - date_of_last_episode)).group(0)
        msg = "Days since last episode:\n\n" + "[" + days + "Days]"
        return await self.bot.say(msg)



def setup(bot):
    bot.add_cog(Hiatus(bot))