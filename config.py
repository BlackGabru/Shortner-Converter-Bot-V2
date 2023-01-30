# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "1466161"))
API_HASH = os.environ.get("API_HASH", "ebc638caaaea23984081ab6625d9c4c0")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "5954482922:AAHsRycW7kdzC9ruUvP1qaQV7oarUTHe5Z4")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split("1382643117")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "playerxdatabase")
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://Aadarsh:Aadarsh07@cluster0.qllzcuy.mongodb.net/?retryWrites=true&w=majority") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "1382643117")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(eagleix)
#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001803407923")) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "PlayerX_Links") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", '') # image when someone hit /start # image when someone hit /start
LINK_BYPASS = "False"
