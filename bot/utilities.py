import discord

from discord import Embed
from itertools import cycle

# Emojis lists to be used in the entire project
positive_emojis_list = cycle(["👍", "🆗", "🤙", "👌", "👊", "🆒", "✅"])
negative_emojis_list = cycle(["🚫", "🛑", "❌", "⛔"])
status_list = cycle(
    [
        "Studying...",
        "--Help",
        "Finding events",
        "Decreasing your grades",
        "Learning new features",
        "Calculating your absences",
        "Learning new libraries",
    ]
)

books_list = cycle(["📚", "📔", "📕", "📖", "📗", "📘", "📙", "📑", "🧾", "📅", "📆", "🗓"])
happy_faces = cycle(["😀", "😁", "😃", "😄", "😅", "😉", "😊", "😋", "😎", "🙂", "🤗", "😛"])

emojis_list = [
    "1️⃣",
    "2️⃣",
    "3️⃣",
    "4️⃣",
    "5️⃣",
    "6️⃣",
    "7️⃣",
    "8️⃣",
    "9️⃣",
]
footer = "Created with 💖 by our team"

thumbnail_url = (
    "https://logodownload.org/wp-content/uploads/2017/09/mackenzie-logo-3.png"
)

url = "https://eadmoodle.mackenzie.br/"

invisible_emoji = "\n<:name:758840767786516520>"

defaultcolor = 0x9F000C

# This file is created to style the bot messages
# Creating a template for messages
def main_messages_style(
    name: str = "",
    message: str = "",
    emote: str = "",
    color: str = "",
    fot: str = "",
    thumb: bool = False,
) -> Embed:
    """Styles for the main messages, it's used in most commands where printing to the user is needed, returns the embedded message"""

    message = f"**{message}**" if message != "" else message
    embed = Embed(
        title=name if name else "",
        description=f"{message} {emote if emote != '' else emote}",
        color=color if color else defaultcolor,
    )

    if thumb:
        embed.set_thumbnail(url=thumbnail_url)

    embed.set_author(name="")
    embed.set_footer(text=fot + footer)
    return embed


# Template message for help
def help_message(contents: list) -> Embed:
    """Returns the help message embedded and styled"""

    embed = Embed(
        title="Standard Commands",
        description="Type `mack help [command]` for more help eg. `mack help get`",
        color=defaultcolor,
    )
    embed.set_thumbnail(url=thumbnail_url)
    embed.set_footer(text=footer)

    for row in range(len(contents)):
        name, value = contents[row][0], ""

        for elem in contents[row][1:]:
            value += f'[`{elem[0]}`{invisible_emoji if row == 0 and contents[row].index(elem) == 3 else ""}]({url} "{elem[1]}")  '

        embed.add_field(name=name, value=value, inline=True)

    return embed


FULL_MONTHS = {
    "janeiro": 1,
    "fevereiro": 2,
    "março": 3,
    "abril": 4,
    "maio": 5,
    "junho": 6,
    "julho": 7,
    "agosto": 8,
    "setembro": 9,
    "outubro": 10,
    "novembro": 11,
    "dezembro": 12,
}


def formatTime(seconds: int) -> str:
    """Fortmats youtube time"""

    hours = seconds // 3600

    seconds %= 3600

    minutes = seconds // 60

    seconds %= 60

    if hours == 0:
        return "%02i:%02i" % (minutes, seconds)
    else:
        return "%02i:%02i:%02i" % (hours, minutes, seconds)


def timeout_message(timeout: float, reaction: bool = False) -> Embed:
    """Returns the embed for the timeout error message"""

    state = "reply" if not reaction else "react"
    return main_messages_style(
        "Timeout error", f"You only have {int(timeout)} seconds to {state}."
    )


def profile_style(
    member: discord.member.Member, ctx: discord.ext.commands.context.Context, **kwargs
) -> Embed:
    """It creates the profile_style embed which is used to show the data to the users"""

    embed = Embed(color=member.color, timestamp=ctx.message.created_at)

    embed.set_thumbnail(url=member.avatar_url)

    embed.set_author(name=f"Profile - {member.display_name}")

    embed.add_field(name="Level", value=f"`{kwargs['user_level']}`")
    embed.add_field(
        name="XP", value=f"`{kwargs['user_experience']}/{kwargs['xp_nextlvl']}`"
    )
    embed.add_field(name="Reputation", value=f"`{kwargs['rep']}`", inline=False)

    embed.add_field(
        name=f"Messages Needed for level {kwargs['user_level'] + 1}",
        value=f"`{kwargs['xp_nextlvl'] - kwargs['user_experience']}`",
        inline=False,
    )

    embed.set_footer(text=f"{member}", icon_url=member.avatar_url)

    return embed
