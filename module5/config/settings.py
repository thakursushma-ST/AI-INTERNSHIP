import os
from dotenv import load_dotenv

load_dotenv()

APP_NAME = "AI Study Assistant"
APP_VERSION = "1.0.0"

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-1.5-flash")

DATA_FILE = os.path.join("data", "conversations.json")
MAX_HISTORY_MESSAGES = 20
