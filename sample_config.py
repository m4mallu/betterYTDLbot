import os

class Config(object):    
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("TG_BOT_TOKEN")
    # Get these values from my.telegram.org
    APP_ID = int(os.environ.get("APP_ID"))
    API_HASH = os.environ.get("API_HASH")
    # Array to store users who are authorized to use the bot
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "").split())
    #Text to be used prior to downloaded videos
    PRE_FILE_TXT = os.environ.get("PRE_FILE_TXT", "@MovieKeralam.")