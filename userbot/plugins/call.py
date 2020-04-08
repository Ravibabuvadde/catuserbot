"""Emoji

Available Commands:

.emoji shrug

.emoji apple

.emoji :/

.emoji -_-"""

from telethon import events

import asyncio


from userbot.utils import admin_cmd

@borg.on(admin_cmd(pattern=f"call", allow_sudo=True))
@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 3

    animation_ttl = range(0, 18)

    input_str = event.pattern_match.group(1)

    if input_str == "call":

        await event.edit(input_str)

        animation_chars = [
        
            "`Connecting To NASA Headquarters...`",
            "`Call Connected.`",
            "`NASA HQ: Hello This is NASA HQ. Who is this?`",
            "`Me: Yo this is` @its_me_einstein ,`Please Connect me to my lil bro,Newton `",
            "`User Authorised.`",
            "`Calling Newton `  `At +919876543210`",
            "`Private  Call Connected...`",
            "`Me: Hello Broo, Please Send ms Gravity Equation .`",    
            "`Newton : May I Know Who Is This?`",
            "`Me: Yo Brah, I Am` @its_me_einstein the Scientist ",
            "`Newton : OMG!!! Long time no see, Wassup einstei ...\nI'll Make Sure The Gravity equation will be sent in 5Mins.`",
            "`Me: Thanks, See You Later Brah.`",
            "`Newton : Please Don't Thank Brah, HQ Is Our's. Just Gimme A Call When You Become Free.`",
            "`Me: Is There Any Issue in Your New Teleportation Equation????`",
            "`Newton : Yes Buddy There is a Small Issue in my Equation \nI Am Not Able To Fix It. If Possible, Please Help Fix The issue.`",
            "`Me: Send Me The Equation On My Telegram Account, I Will Fix The issue & Send You.`",
            "`Newton : Sure Bro \nTC Bye Bye :)`",
            "`Private Call Disconnected.`"
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 18])
