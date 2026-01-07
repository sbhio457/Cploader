import os
from os import environ

# API Configuration
API_ID = int(os.environ.get("API_ID", "28161387"))
API_HASH = os.environ.get("API_HASH", "911b975dad78e1c06faff0ec21cc99a6")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8423500157:AAFRmG9z3OgnThUcakfEZPxS6qwEA_0xF0M")

CREDIT = os.environ.get("CREDIT", "𝐈𝐓'𝐬𝐆𝐎𝐋𝐔")
# MongoDB Configuration
DATABASE_NAME = os.environ.get("DATABASE_NAME", "leonorbrachma_db_user")
DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://leonorbrachma_db_user:<j21Ud1GUOR9WJJjz>@cluster0.ttmqijj.mongodb.net/?appName=Cluster0")  # Add your own atlas db
MONGO_URL = DATABASE_URL  # For auth system

# Owner and Admin Configuration
OWNER_ID = int(os.environ.get("OWNER_ID", "6923038522"))
ADMINS = [int(x) for x in os.environ.get("ADMINS", "").split()]  # Default to owner ID

# Channel Configuration
PREMIUM_CHANNEL = ""
# Thumbnail Configuration
THUMBNAILS = list(map(str, os.environ.get("THUMBNAILS", "").split())) # Image Link For Default Thumbnail 

# Web Server Configuration
WEB_SERVER = os.environ.get("WEB_SERVER", "False").lower() == "true"
WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8000))

# Message Formats
AUTH_MESSAGES = {
    "subscription_active": """<b>🎉 Subscription Activated!</b>

<blockquote>Your subscription has been activated and will expire on {expiry_date}.
You can now use the bot!</blockquote>\n\n Type /start to start uploading """,

    "subscription_expired": """<b>⚠️ Your Subscription Has Ended</b>

<blockquote>Your access to the bot has been revoked as your subscription period has expired.
Please contact the admin to renew your subscription.</blockquote>""",

    "user_added": """<b>✅ User Added Successfully!</b>

<blockquote>👤 Name: {name}
🆔 User ID: {user_id}
📅 Expiry: {expiry_date}</blockquote>""",

    "user_removed": """<b>✅ User Removed Successfully!</b>

<blockquote>User ID {user_id} has been removed from authorized users.</blockquote>""",

    "access_denied": """<b>⚠️ Access Denied!</b>

<blockquote>You are not authorized to use this bot.
Please contact the admin to get access.</blockquote>""",

    "not_admin": "⚠️ You are not authorized to use this command!",
    
    "invalid_format": """❌ <b>Invalid Format!</b>

<blockquote>Use format: {format}</blockquote>"""
}















