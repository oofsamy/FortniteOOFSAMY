import fortnitepy

platform = input("Platform to start bot on: WINDOWS, PLAYSTATION, SWITCH, XBOX, MOBILE: ")
discordPrefix = input("What do you want your Discord bot prefix to be: ")

def checkPlatformCorrect():
    if platform.upper() in ["WINDOWS", "PLAYSTATION", "SWITCH", "XBOX", "MOBILE"]:
        return fortnitepy.Platform[platform]
    else:
        return fortnitepy.Platform.WINDOWS

    print(platform + " has been selected on local client")

def checkPrefixCorrect():
    if discordPrefix == None:
        return "$"
    elif discordPrefix == "":
        return "$"