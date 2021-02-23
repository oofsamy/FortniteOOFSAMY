from functools import partial
import fortnitepy
import discord
from discord.ext import commands
import BenBotAsync
import requests
import json
import os

from fortnitepy.ext import commands as fortnite_commands
from discord.ext import commands as discord_commands

email = 'EPIC GAMES EMAIL'
password = 'EPIC GAMES PASSWORD'
filename = 'device_auths.json'
discord_bot_token = 'DISCORD BOT TOKEN'
description = 'My discord + fortnite bot!'
platform = input("Platform to start bot on: WINDOWS, PLAYSTATION, SWITCH, XBOX, MOBILE: ")
discordPrefix = input("What do you want your Discord bot prefix to be: ")

def imageFortnite(cosmeticId):
    url = "https://fortnite-api.com/v2/cosmetics/br/"+cosmeticId
    r = requests.get(url)
    data = r.text
    data = json.loads(data)
    return data["data"]["images"]["icon"]

def checkPlatformCorrect():
    for x in ["WINDOWS", "PLAYSTATION", "PLAYSTATION", "SWITCH", "XBOX", "MOBILE"]:
        if platform == x:
            return fortnitepy.Platform[platform]
        else:
            return fortnitepy.Platform.WINDOWS
    print(platform + " has been selected on local client")

def checkPrefixCorrect():
    if platform == None:
        return "$"
    elif platform == "":
        return "$"

async def imageFortnite(cosmetic):
    url = " https://fortnite-api.com/v2/cosmetics/br/"

def store_device_auth_details(email, details):
    existing = get_device_auth_details()
    existing[email] = details

    with open(filename, 'w') as fp:
        json.dump(existing, fp)

def get_device_auth_details():
    if os.path.isfile(filename):
        with open(filename, 'r') as fp:
            return json.load(fp)
    return {}

device_auth_details = get_device_auth_details().get(email, {})
fortnite_bot = fortnite_commands.Bot(
    command_prefix='!',
    description=description,
    auth=fortnitepy.AdvancedAuth(
        email=email,
        password=password,
        prompt_authorization_code=True,
        delete_existing_device_auths=True,
        **device_auth_details
    ),
    status="oofsamy lobby bot",
    platform=checkPlatformCorrect()
)

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix=discordPrefix, description="A fortnitepy bot with discord integration made by oofsamy#2714", intents=intents)


@fortnite_bot.event
async def event_ready():
    print('Fortnite bot ready')
    await bot.start(discord_bot_token)

@fortnite_bot.event
async def event_device_auth_generate(details, email):
    store_device_auth_details(email, details)

@fortnite_bot.event
async def event_before_close():
    await bot.close()

@bot.event
async def on_ready():
    print('Discord bot ready')

@bot.command()
async def test(ctx, arg):
    await ctx.send("Test Command Found")
    await fortnite_bot.party.send("Test Command Found")

@bot.command()
async def skin(ctx, arg):
    cont = ctx.message.content[6:len(ctx.message.content)]
    try: 
        cosmetic = await BenBotAsync.get_cosmetic(
            lang="en",
            searchLang="en",
            matchMethod="contains",
            name=cont,
            backendType="AthenaCharacter"
        )
        await fortnite_bot.party.me.set_outfit(asset=cosmetic.id)
        embed=discord.Embed(title="Skin set to " + cosmetic.name)
        embed.set_thumbnail(url=imageFortnite(cosmetic.id))
        nameofbot = fortnite_bot.user.display_name
        embed.add_field(name="Lobby Bot: " + nameofbot, value="made by oofsamy", inline=False)
        await ctx.send(embed=embed)
    except:
        await ctx.send("Cosmetic couldn't be found!")

fortnite_bot.run()