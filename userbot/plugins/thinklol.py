# (c) @UniBorg

from telethon import events
import asyncio
from collections import deque

from userbot.utils import admin_cmd

@borg.on(events.NewMessage(pattern=r"\.lol", outgoing=True))
async def _(event):
	sleepValue = 5
	if event.fwd_from:
		return
	deq = deque(list("🤔🧐🤔🧐🤔🧐"))
	for _ in range(999):
		await asyncio.sleep(0.1)
		await event.edit("".join(deq))
		deq.rotate(1)
    		await asyncio.sleep(sleepValue)
