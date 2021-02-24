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
    if discordPrefix == None:
        return "$"
    elif discordPrefix == "":
        return "$"

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

async def userByName(name):
    print(name)
    iD = await fortnite_bot.fetch_user_by_display_name(name)
    if iD != None:
        print(iD)
        whatTo = iD.id
        return whatTo


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

@fortnite_bot.event
async def event_party_invite(invitiation):
    await invitiation.accept()

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

@bot.command()
async def skinFull(ctx):
    cont = ctx.message.content[10:len(ctx.message.content)]
    cosmetic = await BenBotAsync.get_cosmetic(
        lang="en",
        searchLang="en",
        matchMethod="full",
        name=cont,
        backendType="AthenaCharacter"
    )
    await fortnite_bot.party.me.set_outfit(asset=cosmetic.id)
    embed=discord.Embed(title="Skin set to " + cosmetic.name)
    embed.set_thumbnail(url=imageFortnite(cosmetic.id))
    nameofbot = fortnite_bot.user.display_name
    embed.add_field(name="Lobby Bot: " + nameofbot, value="made by oofsamy", inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def emote(ctx):
    cont = ctx.message.content[7:len(ctx.message.content)]
    try:
        cosmetic = await BenBotAsync.get_cosmetic(
            lang="en",
            searchLang="en",
            matchMethod="contains",
            name=cont,
            backendType="AthenaDance"
        )
        await fortnite_bot.party.me.set_emote(asset=cosmetic.id)
        embed=discord.Embed(title="Emote set to " + cosmetic.name)
        embed.set_thumbnail(url=imageFortnite(cosmetic.id))
        nameofbot = fortnite_bot.user.display_name
        embed.add_field(name="Lobby Bot: " + nameofbot, value="made by oofsamy", inline=False)
        await ctx.send(embed=embed)
    except:
        await ctx.send("Cosmetic couldn't be found!")

@bot.command()
async def emoteFull(ctx):
    cont = ctx.message.content[11:len(ctx.message.content)]
    try:
        cosmetic = await BenBotAsync.get_cosmetic(
            lang="en",
            searchLang="en",
            matchMethod="full",
            name=cont,
            backendType="AthenaDance"
        )
        await fortnite_bot.party.me.set_emote(asset=cosmetic.id)
        embed=discord.Embed(title="Emote set to " + cosmetic.name)
        embed.set_thumbnail(url=imageFortnite(cosmetic.id))
        nameofbot = fortnite_bot.user.display_name
        embed.add_field(name="Lobby Bot: " + nameofbot, value="made by oofsamy", inline=False)
        await ctx.send(embed=embed)
    except:
        await ctx.send("Cosmetic couldn't be found!")

@bot.command()
async def backpack(ctx):
    cont = ctx.message.content[10:len(ctx.message.content)]
    try:
        cosmetic = await BenBotAsync.get_cosmetic(
            lang="en",
            searchLang="en",
            matchMethod="contains",
            name=cont,
            backendType="AthenaBackpack"
        )
        await fortnite_bot.party.me.set_emote(asset=cosmetic.id)
        embed=discord.Embed(title="Backpack set to " + cosmetic.name)
        embed.set_thumbnail(url=imageFortnite(cosmetic.id))
        nameofbot = fortnite_bot.user.display_name
        embed.add_field(name="Lobby Bot: " + nameofbot, value="made by oofsamy", inline=False)
        await ctx.send(embed=embed)
    except:
        await ctx.send("Cosmetic couldn't be found!")

@bot.command()
async def backpackFull(ctx):
    cont = ctx.message.content[14:len(ctx.message.content)]
    print(cont)
    cosmetic = await BenBotAsync.get_cosmetic(
        lang="en",
        searchLang="en",
        matchMethod="full",
        name=cont,
        backendType="AthenaBackpack"
    )
    await fortnite_bot.party.me.set_backpack(asset=cosmetic.id)
    embed=discord.Embed(title="Backpack set to " + cosmetic.name)
    embed.set_thumbnail(url=imageFortnite(cosmetic.id))
    nameofbot = fortnite_bot.user.display_name
    embed.add_field(name="Lobby Bot: " + nameofbot, value="made by oofsamy", inline=False)
    await ctx.send(embed=embed)
    #await ctx.send("Cosmetic couldn't be found!")

@bot.command()
async def pickaxe(ctx):
    cont = ctx.message.content[9:len(ctx.message.content)]
    try:
        cosmetic = await BenBotAsync.get_cosmetic(
            lang="en",
            searchLang="en",
            matchMethod="contains",
            name=cont,
            backendType="AthenaPickaxe"
        )
        await fortnite_bot.party.me.set_emote(asset=cosmetic.id)
        embed=discord.Embed(title="Pickaxe set to " + cosmetic.name + "\n Make sure to do (prefix)emote Point It Out \n to see the pickaxe")
        embed.set_thumbnail(url=imageFortnite(cosmetic.id))
        nameofbot = fortnite_bot.user.display_name
        embed.add_field(name="Lobby Bot: " + nameofbot, value="made by oofsamy", inline=False)
        embed.set_footer(text="Make sure to do $emote Point It Out to see the pickaxe")
        await ctx.send(embed=embed)
    except:
        await ctx.send("Cosmetic couldn't be found!")

@bot.command()
async def pickaxeFull(ctx):
    cont = ctx.message.content[13:len(ctx.message.content)]
    try:
        cosmetic = await BenBotAsync.get_cosmetic(
            lang="en",
            searchLang="en",
            matchMethod="full",
            name=cont,
            backendType="AthenaPickaxe"
        )
        await fortnite_bot.party.me.set_pickaxe(asset=cosmetic.id)
        embed=discord.Embed(title="Pickaxe set to " + cosmetic.name)
        embed.set_thumbnail(url=imageFortnite(cosmetic.id))
        nameofbot = fortnite_bot.user.display_name
        embed.add_field(name="Lobby Bot: " + nameofbot, value="made by oofsamy", inline=False)
        embed.set_footer(text="Make sure to do $emote Point It Out to see the pickaxe")
        await ctx.send(embed=embed)
    except:
        await ctx.send("Cosmetic couldn't be found!")


@bot.command()
async def promote(ctx, arg):
    playerId = await userByName(ctx.message.content[9:])
    player = fortnite_bot.party.get_member(playerId)
    await player.promote()


@bot.command()
async def ready(ctx):
    if fortnite_bot.is_ready == True:
        await ctx.send(fortnite_bot.party.me.display_name + " is already ready")
    else:
        await fortnite_bot.party.me.set_ready(fortnitepy.ReadyState.READY)
    #fortnitepy.ReadyState

@bot.command()
async def setStatus(ctx, arg):
    if arg.lower() == "fortnite":
        await fortnite_bot.set_presence(ctx.message.content[20:])
        await ctx.send("Status on fortnite is set to " + ctx.message.content[20:])
    elif arg.lower() == "discord":
        game = discord.Game(ctx.message.content[19:])
        await bot.change_presence(activity=game)
        await ctx.send("Status on discord is set to " + ctx.message.content[19:])
    elif arg.lower() == "both":
        await ctx.send("Status on both fortnite and discord are set to "+ctx.message.content[11:])
        game = discord.Game(ctx.message.content[16:])
        await fortnite_bot.set_presence(ctx.message.content[16:])
        await bot.change_presence(activity=game)
        await ctx.send("Status on both fortnite and discord are set to "+ctx.message.content[16:])
    else:
        await ctx.send("Please specify what platform you want to change the status on \nExample: ``$setStatus fortnite`` \nAvailable parameters are ``fortnite`` ``discord`` ``both``")

fortnite_bot.run()