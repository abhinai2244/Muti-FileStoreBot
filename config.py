#@cantarellabots

import os
import sys
import logging
from logging.handlers import RotatingFileHandler

# =============================================================================
# REQUIRED CONFIGURATION — Must be set before running
# =============================================================================

# Telegram API credentials from https://my.telegram.org
API_ID = int(os.environ.get("API_ID", "22876298"))
APP_ID = API_ID # Alias for backward compatibility
API_HASH = os.environ.get("API_HASH", "cda7be15fbe283b5b97e8fb8c4233e36")
#@cantarellabots
# Main controller bot token from @BotFather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8863511609:AAFVdDpKstUnpjAxw7Asaqh_JsB6HtJb9O0")
TG_BOT_TOKEN = BOT_TOKEN # Alias for backward compatibility
#@cantarellabots
# Owner's Telegram user ID (numeric)
OWNER_ID = int(os.environ.get("OWNER_ID", "8340629952"))

# MongoDB connection URI
MONGO_URI = os.environ.get("MONGO_URI", "mongodb+srv://CINEDISQ_db:GkUTuhQGy2n3aFdx@cluster0.me5ktq2.mongodb.net/?appName=Cluster0")
MONGO_DB_NAME = os.environ.get("MONGO_DB_NAME", "CINEDISQ_db")
DB_URI = MONGO_URI    # Alias for old bot.py
DB_NAME = MONGO_DB_NAME # Alias for old bot.py

# Placeholder for old bot.py
CHANNEL_ID = 1003947471625

# Central log channel for logging bot creations and generated links
MAIN_LOG_CHANNEL = int(os.environ.get("MAIN_LOG_CHANNEL", "-1003951903260"))

# Force-subscribe channel for the main bot (username without @)
FSUB_CHANNEL = os.environ.get("FSUB_CHANNEL", "cinedisq") 

# =============================================================================
# ENCRYPTION — Used to secure bot tokens in the database
# =============================================================================

# Fernet encryption key (generate one with: python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())")
# If not set, a default key will be generated on first run (NOT recommended for production)
ENCRYPTION_KEY = os.environ.get("ENCRYPTION_KEY", "")

# API URL for Permanent Link Feature
# Point this to your Cloudflare Worker URL

BACKEND_API_URL = os.environ.get("BACKEND_API_URL", "")
BACKEND_API_SECRET = os.environ.get("BACKEND_API_SECRET", "")
# =============================================================================
# OPTIONAL CONFIGURATION
# =============================================================================

# Number of Pyrogram workers for the main bot
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "8"))

# Web server port (for health checks / keep-alive)
PORT = int(os.environ.get("PORT", "8080"))

# Maximum number of bots a single user can create
MAX_BOTS_PER_USER = int(os.environ.get("MAX_BOTS_PER_USER", "1"))

# Default auto-delete time for files (in seconds, 0 = disabled)
DEFAULT_AUTO_DELETE = int(os.environ.get("DEFAULT_AUTO_DELETE", "0"))

# Rate limiting: minimum seconds between bot creation attempts
BOT_CREATION_COOLDOWN = int(os.environ.get("BOT_CREATION_COOLDOWN", "30"))

# Hibernation: auto-stop idle bots after this many hours (lower = more RAM savings)
HIBERNATION_HOURS = int(os.environ.get("HIBERNATION_HOURS", "48"))

# =============================================================================
# UI TEXTS
# =============================================================================

START_PIC = os.environ.get(
    "START_PIC",
    "https://ibb.co/95CW1J7"
)

FORCE_PIC = os.environ.get(
    "FORCE_PIC",
    "https://ibb.co/mFJY2bhx"
)

START_MSG = """<b>━━━━━━━━━━━━━━━━━━━━━
⚡ 𝗖𝗔𝗡𝗧𝗔𝗥𝗘𝗟𝗟𝗔 𝗙𝗜𝗟𝗘𝗦𝗧𝗢𝗥𝗘 ⚡
━━━━━━━━━━━━━━━━━━━━━</b>

<blockquote>ᴡᴇʟᴄᴏᴍᴇ, {mention}!

ɪ ᴀᴍ ᴀ <b>ᴘʀᴇᴍɪᴜᴍ ᴍᴜʟᴛɪ-ᴜsᴇʀ ꜰɪʟᴇsᴛᴏʀᴇ</b> ᴘʟᴀᴛꜰᴏʀᴍ.
ᴄʀᴇᴀᴛᴇ ʏᴏᴜʀ ᴏᴡɴ ꜰɪʟᴇsᴛᴏʀᴇ ʙᴏᴛ ɪɴ sᴇᴄᴏɴᴅs!

╭─── ✦ ꜰᴇᴀᴛᴜʀᴇs ✦ ───╮
│ ◈ ꜰɪʟᴇ sᴛᴏʀᴀɢᴇ ᴡɪᴛʜ sʜᴀʀᴇ ʟɪɴᴋs
│ ◈ ꜰᴏʀᴄᴇ sᴜʙsᴄʀɪʙᴇ ᴄʜᴀɴɴᴇʟs
│ ◈ ᴜʀʟ sʜᴏʀᴛᴇɴᴇʀ ɪɴᴛᴇɢʀᴀᴛɪᴏɴ
│ ◈ ᴀᴅᴍɪɴ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ
│ ◈ ᴀᴜᴛᴏ-ᴅᴇʟᴇᴛᴇ ᴛɪᴍᴇʀ
│ ◈ ꜰᴏʀᴍᴀᴛᴛᴇᴅ ʟɪɴᴋ ɢᴇɴᴇʀᴀᴛᴏʀ
╰──────────────────╯</blockquote>

<i>⬇️ ᴛᴀᴘ ᴀ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ sᴛᴀʀᴛᴇᴅ ⬇️</i>"""

HELP_MSG = """<b>━━━━━━━━━━━━━━━━━━━━━
📖 𝗛𝗘𝗟𝗣 & 𝗚𝗨𝗜𝗗𝗘
━━━━━━━━━━━━━━━━━━━━━</b>

<blockquote><b>⚙️ ʜᴏᴡ ᴛᴏ ᴄʀᴇᴀᴛᴇ ʏᴏᴜʀ ʙᴏᴛ:</b>

<b>❶</b> ᴛᴀᴘ <b>⚡ ᴄʀᴇᴀᴛᴇ ʙᴏᴛ</b>
<b>❷</b> sᴇɴᴅ ʏᴏᴜʀ ʙᴏᴛ ᴛᴏᴋᴇɴ (ꜰʀᴏᴍ @BotFather)
<b>❸</b> sᴇɴᴅ ʏᴏᴜʀ ʟᴏɢ ᴄʜᴀɴɴᴇʟ ɪᴅ
<b>❹</b> ʏᴏᴜʀ ʙᴏᴛ sᴛᴀʀᴛs ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ!</blockquote>

<blockquote><b>🎛 ᴅᴀsʜʙᴏᴀʀᴅ ꜰᴇᴀᴛᴜʀᴇs:</b>

◈ <b>ꜰᴏʀᴄᴇ sᴜʙsᴄʀɪʙᴇ</b> — ᴀᴅᴅ ᴄʜᴀɴɴᴇʟs
◈ <b>ᴜʀʟ sʜᴏʀᴛᴇɴᴇʀ</b> — ᴍᴏɴᴇᴛɪᴢᴇ ʟɪɴᴋs
◈ <b>ᴀᴅᴍɪɴ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ</b> — ᴀᴅᴅ/ʀᴇᴍᴏᴠᴇ ᴀᴅᴍɪɴs
◈ <b>sᴛᴀᴛɪsᴛɪᴄs</b> — ᴠɪᴇᴡ ᴜsᴀɢᴇ sᴛᴀᴛs
◈ <b>ᴀᴜᴛᴏ-ᴅᴇʟᴇᴛᴇ</b> — sᴇᴛ ᴛɪᴍᴇʀ
◈ <b>sᴛᴀʀᴛ ᴄᴏɴꜰɪɢ</b> — ᴄᴜsᴛᴏᴍ ᴡᴇʟᴄᴏᴍᴇ</blockquote>

<blockquote><b>📌 ᴡᴏʀᴋᴇʀ ʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅs:</b>

<code>/start</code> — sᴛᴀʀᴛ / ʀᴇᴛʀɪᴇᴠᴇ ꜰɪʟᴇs
<code>/genlink</code> — ʟɪɴᴋ ꜰᴏʀ ᴀ sɪɴɢʟᴇ ᴘᴏsᴛ
<code>/batch</code> — ʟɪɴᴋ ꜰᴏʀ ᴍᴜʟᴛɪᴘʟᴇ ᴘᴏsᴛs
<code>/custom_batch</code> — ᴄᴜsᴛᴏᴍ ʙᴀᴛᴄʜ
<code>/flink</code> — ꜰᴏʀᴍᴀᴛᴛᴇᴅ ʟɪɴᴋs
<code>/ban</code> · <code>/unban</code> — ᴜsᴇʀ ᴍᴏᴅᴇʀᴀᴛɪᴏɴ</blockquote>"""

ABOUT_MSG = """<b>━━━━━━━━━━━━━━━━━━━━━
ℹ️ 𝗔𝗕𝗢𝗨𝗧
━━━━━━━━━━━━━━━━━━━━━</b>

<blockquote><b>⚡ ᴄᴀɴᴛᴀʀᴇʟʟ ꜰɪʟᴇsᴛᴏʀᴇ ᴠ3.0</b>

ᴀ ᴘʀᴇᴍɪᴜᴍ ᴍᴜʟᴛɪ-ᴜsᴇʀ ᴛᴇʟᴇɢʀᴀᴍ
ꜰɪʟᴇsᴛᴏʀᴇ ᴘʟᴀᴛꜰᴏʀᴍ.

╭─── ✦ ʜɪɢʜʟɪɢʜᴛs ✦ ───╮
│ ◈ ɪsᴏʟᴀᴛᴇᴅ ʙᴏᴛ ɪɴsᴛᴀɴᴄᴇs
│ ◈ ᴇɴᴄʀʏᴘᴛᴇᴅ ᴛᴏᴋᴇɴ sᴛᴏʀᴀɢᴇ
│ ◈ ꜰᴏʀᴄᴇ sᴜʙ (ᴊᴏɪɴ + ʀᴇǫᴜᴇsᴛ)
│ ◈ ᴜʀʟ sʜᴏʀᴛᴇɴᴇʀ
│ ◈ ᴀᴜᴛᴏ-ᴅᴇʟᴇᴛᴇ & ᴀᴅᴍɪɴ
│ ◈ ꜰᴏʀᴍᴀᴛᴛᴇᴅ ʟɪɴᴋ ɢᴇɴ
│ ◈ ᴀᴜᴛᴏ-ʜɪʙᴇʀɴᴀᴛɪᴏɴ
╰──────────────────╯

<b>ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ</b> @cantarellabots</blockquote>"""

FORCE_MSG = """<b>━━━━━━━━━━━━━━━━━━━━━
🔒 𝗔𝗖𝗖𝗘𝗦𝗦 𝗥𝗘𝗦𝗧𝗥𝗜𝗖𝗧𝗘𝗗
━━━━━━━━━━━━━━━━━━━━━</b>

<blockquote>ʜᴇʏ {mention},

ᴛᴏ ᴜsᴇ ᴛʜɪs ʙᴏᴛ ʏᴏᴜ ᴍᴜsᴛ ᴊᴏɪɴ ᴏᴜʀ ᴄʜᴀɴɴᴇʟ ꜰɪʀsᴛ.
ᴛᴀᴘ ᴛʜᴇ ʙᴜᴛᴛᴏɴ ʙᴇʟᴏᴡ ᴀɴᴅ ᴄʟɪᴄᴋ <b>♻️ ʀᴇʟᴏᴀᴅ</b>.</blockquote>"""

# =============================================================================
# LOGGING
# =============================================================================

LOG_FILE = "filestore_multi.log"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(LOG_FILE, maxBytes=50_000_000, backupCount=5, encoding="utf-8"),
        logging.StreamHandler(sys.stdout)
    ],
)

# Suppress noisy loggers
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("pymongo").setLevel(logging.WARNING)
logging.getLogger("motor").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    """Return a named logger instance."""
    return logging.getLogger(name)
