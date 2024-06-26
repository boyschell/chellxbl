from Auput.core.bot import AuputBot
from Auput.core.dir import dirr
from Auput.core.git import git
from Auput.core.userbot import Userbot
from Auput.misc import dbb, sudo

from .logging import LOGGER

# Directories
dirr()

# Check Git Updates
git()

# Initialize Memory DB
dbb()

# Heroku APP
#heroku()

# Load Sudo Users from DB
sudo()

# Bot Client
app = AuputBot()

# Assistant Client
userbot = Userbot()

from .platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()
