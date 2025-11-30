#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "29754330"))
API_HASH = environ.get("API_HASH", "6d58372712767f434c30ecfa3cb1951e")
BOT_TOKEN = environ.get("BOT_TOKEN", "8524064780:AAGqeh7cr1tRIC0aQvNUNZqXFeF1RZIlcVc")

OWNER = int(environ.get("OWNER", "7052558926"))
CREDIT = environ.get("CREDIT", "ARGHYDEEP")
cookies_file_path = os.getenv("cookies_file_path", "youtube_cookies.txt")

TOTAL_USER = os.environ.get('TOTAL_USERS', '7052558926').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '7052558926').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
# .....,.....,.......,...,.......,....., .....,.....,.......,...,.......,.....,
api_url = "https://head-micheline-botupdatevip-f1804c58.koyeb.app/get_keys?url={url}@botupdatevip4u&user_id=7052558926&token=7051wYX5M7k8Gi640g4"
api_token = "7051wYX5M7k8Gi640g4"
# .....,.....,.......,...,.......,....., .....,.....,.......,...,.


