# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
import json
import os

def get_user_list(config, key):
    with open('{}/tg_bot/{}'.format(os.getcwd(), config), 'r') as json_file:
        return json.load(json_file)[key]


# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True

    # REQUIRED
    API_KEY = "YOUR BOT TOKEN HERE"
    OWNER_ID = "YOUR OWN ID HERE"  # If you dont know, run the bot and do /id in your private chat with it
    OWNER_USERNAME = "YOUR USERNAME HERE"

    # RECOMMENDED
    MESSAGE_DUMP = None  # needed to make sure 'save from' messages persist
    GBAN_LOGS = None #Channel ID here with -
    FED_LOGS = None #Channel ID here with -
    LOAD = []
    NO_LOAD = ['translation', 'rss']
    URL = None

    # OPTIONAL
    #ID Seperation format [1,2,3,4]
    SUDO_USERS = get_user_list('elevated_users.json', 'sudos')  # List of id's -  (not usernames) for users which have sudo access to the bot.
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = False  #Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = False
    WORKERS = 8  # Number of subthreads to use. Set as number of threads your processor uses
    BAN_STICKER = 'CAADAgADOwADPPEcAXkko5EB3YGYAg'  # banhammer marie sticker
    ALLOW_EXCL = False  # Allow ! commands as well as /


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
