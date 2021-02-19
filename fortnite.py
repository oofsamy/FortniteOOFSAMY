from functools import partial
import fortnitepy
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
platform = input("Platform to start bot on: WINDOWS, PLAYSTATION, SWITCH, XBOX, MOBILE")


def checkPlatformCorrect():
    for x in ["WINDOWS", "PLAYSTATION", "PLAYSTATION", "SWITCH", "XBOX", "MOBILE"]:
        if platform == x:
            return platform
        else:
            return fortnitepy.Platform.WINDOWS
    print(platform)

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