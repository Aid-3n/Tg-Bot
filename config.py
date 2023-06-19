# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "2468192"))
API_HASH = os.environ.get("API_HASH", "4906b3f8f198ec0e24edb2c197677678")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "5976917486:AAHr8Bge8lQmSdMgT3mH5al8jmHu1-d1ktw")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split("2068233407")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluster0")
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://yashugowda0003:CVPi63tdQJwS0xw5@cluster0.26a0ose.mongodb.net/?retryWrites=true&w=majority") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "2068233407")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(2068233407)
#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001693006436")) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "syshort") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", '') # image when someone hit /start # image when someone hit /start
LINK_BYPASS = "False"
