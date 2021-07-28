import os
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
  load_dotenv("local.env")

SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "Veez Music Bot")
BOT_USERNAME = getenv("BOT_USERNAME", "veezmusicbot")

BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/d91623e9cefcef8fb3aa8.png")
PROJECT_NAME = getenv("PROJECT_NAME", "Veez Music Project")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "levinachannel")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "gcsupportbots")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "veezasisstant")
OWNER = getenv("OWNER", "@dlwrml")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
