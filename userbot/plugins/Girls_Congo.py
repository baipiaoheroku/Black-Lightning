

import random

from uniborg.util import edit_or_reply, admin_cmd, sudo_cmd

from userbot import CMD_HELP

RUNSREACTS = [
    "`Congratulations and BRAVO SIS!`",
    "`Aww Sis You did it! So proud of you Congo!`",
    "`OMG Sis This calls for celebrating! Congratulations!`",
    "`I knew it was only a matter of time. Well done!`",
    "`Congratulations on your well-deserved success.`",
    "`Heartfelt congratulations to you.`",
    "`Warmest congratulations on your achievement.`",
    "`Congratulations and best wishes for your next adventure!”`",
    "`So pleased to see you accomplishing great things.`",
    "`Feeling so much joy for you today. What an impressive achievement!`",
]


@borg.on(admin_cmd(pattern="Gcongo"))
@borg.on(sudo_cmd(pattern="Gcongo", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    bro = random.randint(0, len(RUNSREACTS) - 1)
    reply_text = RUNSREACTS[bro]
    await edit_or_reply(event, reply_text)


CMD_HELP.update(
    {
        "congratulations": "**Congratulations**\
\n\n**Syntax : **`.Gcongo`\
\n**Usage :** This plugin is used Fir Girls To Congratulate Someone."
    }
)