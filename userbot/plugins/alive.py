"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "cat"

@command(outgoing=True, pattern="^.alive$")
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.edit("**MY BOT IS RUNNING SUCCESFULLY**\n\n"
                     "`Telethon version: 1.11.3\nPython: 3.8.2\nBot was build by:` @its_me_einstein\n"
                     "`fork by :` [Einstein](tg://user?id=1014625158)\n"
                     "`Database Status: Databases functioning normally!\n\nAlways with you, my master!\n`"
                     f"`My peru owner`: {DEFAULTUSER}\n"
                     #"[Deploy this userbot Now](https://github.com/sandy1709/userbot)"
                    )
