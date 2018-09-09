import discord
from discord.ext import commands
import urllib.request
import json
import os

BOT_TOKEN = os.environ["BOT_TOKEN"]

bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    print(bot.user.name)
    print(bot.user.id)

@bot.command()
async def stage(ctx, arg):
    api_url = "https://spla2.yuu26.com/schedule"
    headers = { "User-Agent" :  "DiscordSplatoon2StageBot/0.1 (@tokoro10g)" }

    result = json.loads(urllib.request.urlopen(urllib.request.Request(api_url, None, headers)).read())["result"]

    idx = 1 if arg == "next" else 0

    str_gachi_rule  = result["gachi"][idx]["rule"]
    str_league_rule = result["league"][idx]["rule"]

    str_regular = ", ".join(result["regular"][idx]["maps"])
    str_gachi   = ", ".join(result["gachi"][idx]["maps"])
    str_league  = ", ".join(result["league"][idx]["maps"])

    await bot.say('''\
```asciidoc
[レギュラーマッチ]
%s

[ガチマッチ(%s)]
%s

[リーグマッチ(%s)]
%s
```\
        ''' % (str_regular, str_gachi_rule, str_gachi, str_league_rule, str_league))

bot.run(BOT_TOKEN)
