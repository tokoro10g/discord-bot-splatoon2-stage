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
async def stage():
    api_url = "https://spla2.yuu26.com/schedule"
    headers = { "User-Agent" :  "DiscordSplatoon2StageBot/0.1 (@tokoro10g)" }

    result = json.loads(urllib.request.urlopen(urllib.request.Request(api_url, None, headers)).read())["result"]

    str_gachi_rule  = result["gachi"][0]["rule"]
    str_league_rule = result["league"][0]["rule"]

    str_regular = ", ".join(result["regular"][0]["maps"])
    str_gachi   = ", ".join(result["gachi"][0]["maps"])
    str_league  = ", ".join(result["league"][0]["maps"])

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
