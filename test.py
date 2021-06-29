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