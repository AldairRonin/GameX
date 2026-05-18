from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
RAWG_API_KEY = os.getenv("RAWG_API_KEY")