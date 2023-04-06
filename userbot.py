from pyrogram import Client, filters, errors, enums
from pyrogram import idle
from config import *


User = Client(name="user-account",
              session_string=SESSION,
              api_id=API_ID,
              api_hash=API_HASH,
              #Removed
              workers=300
              )



