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
client = fortnite_commands.Bot(
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
    iD = await client.fetch_user_by_display_name(name)
    if iD != None:
        print(iD)
        whatTo = iD.id
        return whatTo


@client.event
async def event_ready():
    print('Fortnite bot ready')
    await bot.start(discord_bot_token)

@client.event
async def event_device_auth_generate(details, email):
    store_device_auth_details(email, details)

@client.event
async def event_before_close():
    await bot.close()

@client.event
async def event_party_invite(invitiation):
    await invitiation.accept()

@bot.event
async def on_ready():
    print('Discord bot ready')

@bot.command()
async def skin(ctx, *, cont):
    try: 
        cosmetic = await BenBotAsync.get_cosmetic(
            lang="en",
            searchLang="en",
            matchMethod="contains",
            name=cont,
            backendType="AthenaCharacter"
        )
        await client.party.me.set_outfit(asset=cosmetic.id)
        embed=discord.Embed(title="Skin set to " + cosmetic.name)
        embed.set_thumbnail(url=imageFortnite(cosmetic.id))
        nameofbot = client.user.display_name
        embed.add_field(name="Lobby Bot: " + nameofbot, value="made by oofsamy", inline=False)
        await ctx.send(embed=embed)
    except:
        await ctx.send("Cosmetic couldn't be found!")

@bot.command()
async def skinFull(ctx, *, cont):
    cosmetic = await BenBotAsync.get_cosmetic(
        lang="en",
        searchLang="en",
        matchMethod="full",
        name=cont,
        backendType="AthenaCharacter"
    )
    await client.party.me.set_outfit(asset=cosmetic.id)
    embed=discord.Embed(title="Skin set to " + cosmetic.name)
    embed.set_thumbnail(url=imageFortnite(cosmetic.id))
    nameofbot = client.user.display_name
    embed.add_field(name="Lobby Bot: " + nameofbot, value="made by oofsamy", inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def emote(ctx, *, cont):
    try:
        cosmetic = await BenBotAsync.get_cosmetic(
            lang="en",
            searchLang="en",
            matchMethod="contains",
            name=cont,
            backendType="AthenaDance"
        )
        await client.party.me.set_emote(asset=cosmetic.id)
        embed=discord.Embed(title="Emote set to " + cosmetic.name)
        embed.set_thumbnail(url=imageFortnite(cosmetic.id))
        nameofbot = client.user.display_name
        embed.add_field(name="Lobby Bot: " + nameofbot, value="made by oofsamy", inline=False)
        await ctx.send(embed=embed)
    except:
        await ctx.send("Cosmetic couldn't be found!")

@bot.command()
async def emoteFull(ctx, *, cont):
    try:
        cosmetic = await BenBotAsync.get_cosmetic(
            lang="en",
            searchLang="en",
            matchMethod="full",
            name=cont,
            backendType="AthenaDance"
        )
        await client.party.me.set_emote(asset=cosmetic.id)
        embed=discord.Embed(title="Emote set to " + cosmetic.name)
        embed.set_thumbnail(url=imageFortnite(cosmetic.id))
        nameofbot = client.user.display_name
        embed.add_field(name="Lobby Bot: " + nameofbot, value="made by oofsamy", inline=False)
        await ctx.send(embed=embed)
    except:
        await ctx.send("Cosmetic couldn't be found!")

@bot.command()
async def backpack(ctx, *, cont):
    try:
        cosmetic = await BenBotAsync.get_cosmetic(
            lang="en",
            searchLang="en",
            matchMethod="contains",
            name=cont,
            backendType="AthenaBackpack"
        )
        await client.party.me.set_emote(asset=cosmetic.id)
        embed=discord.Embed(title="Backpack set to " + cosmetic.name)
        embed.set_thumbnail(url=imageFortnite(cosmetic.id))
        nameofbot = client.user.display_name
        embed.add_field(name="Lobby Bot: " + nameofbot, value="made by oofsamy", inline=False)
        await ctx.send(embed=embed)
    except:
        await ctx.send("Cosmetic couldn't be found!")

@bot.command()
async def backpackFull(ctx, *, cont):
    cosmetic = await BenBotAsync.get_cosmetic(
        lang="en",
        searchLang="en",
        matchMethod="full",
        name=cont,
        backendType="AthenaBackpack"
    )
    await client.party.me.set_backpack(asset=cosmetic.id)
    embed=discord.Embed(title="Backpack set to " + cosmetic.name)
    embed.set_thumbnail(url=imageFortnite(cosmetic.id))
    nameofbot = client.user.display_name
    embed.add_field(name="Lobby Bot: " + nameofbot, value="made by oofsamy", inline=False)
    await ctx.send(embed=embed)
    #await ctx.send("Cosmetic couldn't be found!")

@bot.command()
async def pickaxe(ctx, *, cont):
    try:
        cosmetic = await BenBotAsync.get_cosmetic(
            lang="en",
            searchLang="en",
            matchMethod="contains",
            name=cont,
            backendType="AthenaPickaxe"
        )
        await client.party.me.set_emote(asset=cosmetic.id)
        embed=discord.Embed(title="Pickaxe set to " + cosmetic.name + "\n Make sure to do (prefix)emote Point It Out \n to see the pickaxe")
        embed.set_thumbnail(url=imageFortnite(cosmetic.id))
        nameofbot = client.user.display_name
        embed.add_field(name="Lobby Bot: " + nameofbot, value="made by oofsamy", inline=False)
        embed.set_footer(text="Make sure to do $emote Point It Out to see the pickaxe")
        await ctx.send(embed=embed)
    except:
        await ctx.send("Cosmetic couldn't be found!")

@bot.command()
async def pickaxeFull(ctx, *, cont):
    try:
        cosmetic = await BenBotAsync.get_cosmetic(
            lang="en",
            searchLang="en",
            matchMethod="full",
            name=cont,
            backendType="AthenaPickaxe"
        )
        await client.party.me.set_pickaxe(asset=cosmetic.id)
        embed=discord.Embed(title="Pickaxe set to " + cosmetic.name)
        embed.set_thumbnail(url=imageFortnite(cosmetic.id))
        nameofbot = client.user.display_name
        embed.add_field(name="Lobby Bot: " + nameofbot, value="made by oofsamy", inline=False)
        embed.set_footer(text="Make sure to do $emote Point It Out to see the pickaxe")
        await ctx.send(embed=embed)
    except:
        await ctx.send("Cosmetic couldn't be found!")


@bot.command()
async def promote(ctx, *, name):
    player = client.party.get_member(name)
    await player.promote()


@bot.command()
async def ready(ctx):
    if client.is_ready == True:
        await ctx.send(client.party.me.display_name + " is already ready")
    else:
        await client.party.me.set_ready(fortnitepy.ReadyState.READY)
    #fortnitepy.ReadyState

@bot.command()
async def setStatus(ctx, platform, *, status):
    if platform.lower() == "fortnite":
        await client.set_presence(status)
        await ctx.send("Status on fortnite is set to " + status)
    elif platform.lower() == "discord":
        game = discord.Game(status)
        await bot.change_presence(activity=game)
        await ctx.send("Status on discord is set to " + status)
    elif platform.lower() == "both":
        await ctx.send("Status on both fortnite and discord are set to "+status)
        game = discord.Game(status)
        await client.set_presence(status)
        await bot.change_presence(activity=game)
        await ctx.send("Status on both fortnite and discord are set to "+status)
    else:
        await ctx.send("Please specify what platform you want to change the status on \nExample: ``$setStatus fortnite`` \nAvailable parameters are ``fortnite`` ``discord`` ``both``")

@bot.command()
async def addFriend(ctx, arg):
    try:      
        player = await client.fetch_user_by_display_name(ctx.message.content[11:])
        await player.add()
    except:
        await ctx.send("Couldn't add friend, try again later!")


@bot.command()
async def leave(ctx):
    sendingString = ""
    playerList = []
    amount = 1
    for x in client.party.members:
        if x.display_name == client.party.me.display_name:
            print("own bot found")
        else:
            playerList.append(x.display_name)
    for x in playerList:
        if amount == len(playerList):
            sendingString = sendingString + x
        else:
            amount += 1 
            sendingString = sendingString + x +", "
    await client.party.me.leave()
    embed=discord.Embed(title="has left the party containing:", description=sendingString)
    embed.set_author(name=client.party.me.display_name)
    await ctx.send(embed=embed)

@bot.command()
async def copy(ctx):
    user = client.party.me
    member = client.party.get_member(await userByName(ctx.message.content[6:])) #6
    if user != None:
        if member.emote == None:
            await client.party.me.edit_and_keep(
                partial(
                    fortnitepy.ClientPartyMember.set_outfit,
                    asset=member.outfit,
                    variants=member.outfit_variants
                ),
                partial(
                    fortnitepy.ClientPartyMember.set_backpack,
                    asset=member.backpack,
                    variants=member.backpack_variants
                ),
                partial(
                    fortnitepy.ClientPartyMember.set_pickaxe,
                    asset=member.pickaxe,
                    variants=member.pickaxe_variants
                )
            )
        else:
            await client.party.me.edit_and_keep(
                partial(
                    fortnitepy.ClientPartyMember.set_outfit,
                    asset=member.outfit,
                    variants=member.outfit_variants
                ),
                partial(
                    fortnitepy.ClientPartyMember.set_backpack,
                    asset=member.backpack,
                    variants=member.backpack_variants
                ),
                partial(
                    fortnitepy.ClientPartyMember.set_pickaxe,
                    asset=member.pickaxe,
                    variants=member.pickaxe_variants
                ),
                partial(
                    fortnitepy.ClientPartyMember.set_emote,
                    asset=member.emote
                )
        )
        await ctx.send("Cosmetics have been copied from "+member.display_name+" and applied to "+client.party.me.display_name)

@bot.command()
async def repeat(ctx):
    partyy = client.party
    await partyy.send("\n"+ctx.message.content[8:]+"\n-"+ctx.author.display_name)

@bot.command()
async def clearEmote(ctx):
    await client.party.me.clear_emote()

@bot.command()
async def clearBackpack(ctx):
    await client.party.me.clear_backpack()

@bot.command()
async def restart(ctx):
    await client.restart()
    await ctx.send(client.party.me.display_name + " is now restarting, please wait for it to connect to Fortnite's endpoints")

@bot.command()
async def arenaHype(ctx, season, *, name):
    name = urllib.parse.quote(name)
    url = ("https://fort-api.com/arena/"+name)
    r = requests.get(url)
    data = r.text
    data = json.loads(data)
    if data[season]:
        await ctx.send("Division: "+data[season]["division"]+"\nLeague: "+data[season]["league"])


client.run()