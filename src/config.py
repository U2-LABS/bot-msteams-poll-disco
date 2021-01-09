import os
from dotenv import load_dotenv


load_dotenv()

SOURCE_NUMBER_OF_SONGS = 25
DEFAULT_TOP_COMMAND_SONGS = 3
DEFAULT_POPTOP_COMMAND_SONGS = 1

class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "")
