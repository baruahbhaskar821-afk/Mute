#!/usr/bin/env python3

import json
import asyncio
import time
import random
import logging
import os
import sys

from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters

# ================= CONFIG =================

BOT_TOKEN = os.environ.get("8799947913:AAEHZfbm1z5ReIsQkBMBxdknX9ObEu08VaY")
OWNER_ID = int(os.environ.get("OWNER_ID", "8568230592"))
DATA_FILE = "data/users.json"

# Ensure data directory exists
os.makedirs("data", exist_ok=True)

SPEED_DELAY = 0.001
EVERYONE_DELAY = 1.2
EVERYONE_BATCH = 5
MAX_STICKER = 100
MAX_SPAM = 20
SPAM_DELAY = 0.4

logging.basicConfig(
    format="%(asctime)s | %(levelname)s | %(message)s",
    level=logging.INFO,
    handlers=[
        logging.FileHandler("geto.log"),
        logging.StreamHandler()
    ]
)

log = logging.getLogger("GETO")

SPAM_RUNNING = {}

# ================= DATA FUNCTIONS =================

def load_data():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        data = {
            "sudo_users": [],
            "mute_delete": [],
            "tmute": {},
            "stickers": [],
            "shayari": {
                "love": [],
                "sad": [],
                "birthday": []
            }
        }
        save_data(data)
        return data
    except Exception:
        return {
            "sudo_users": [],
            "mute_delete": [],
            "tmute": {},
            "stickers": [],
            "shayari": {
                "love": [],
                "sad": [],
                "birthday": []
            }
        }


def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)


def is_owner(uid):
    return uid == OWNER_ID


def is_sudo(uid, data):
    return uid == OWNER_ID or uid in data.get("sudo_users", [])


def get_mention(user):
    if user.username:
        return f"@{user.username}"
    return f"{user.first_name}"


# ================= MAIN BOT =================

async def main():

    print("GETO BOT RUNNING")

    app = Application.builder().token(8799947913:AAEHZfbm1z5ReIsQkBMBxdknX9ObEu08VaY).build()

    await app.initialize()
    await app.start()

    await app.updater.start_polling()

    while True:
        await asyncio.sleep(1)


# ================= START =================

if __name__ == "__main__":
    asyncio.run(main())
