from discord.ext import commands
import discord.utils


#
# This is a modified version of checks.py, originally made by Rapptz
#
#                 https://github.com/Rapptz
#          https://github.com/Rapptz/RoboDanny/tree/async
#

def is_owner_check(ctx):
    _id = ctx.message.author.id
    return _id == ctx.bot.settings.owner or _id in ctx.bot.settings.co_owners

def is_owner():
    return commands.has_role('administrator')

# The permission system of the bot is based on a "just works" basis
# You have permissions and the bot has permissions. If you meet the permissions
# required to execute the command (and the bot does as well) then it goes through
# and you can execute the command.
# If these checks fail, then there are two fallbacks.
# A role with the name of Bot Mod and a role with the name of Bot Admin.
# Having these roles provides you access to certain commands without actually having
# the permissions required for them.
# Of course, the owner will always be able to execute commands.


def admin_or_permissions():
    return commands.has_permissions(administrator=True)

def admin():
    return admin_or_permissions()

