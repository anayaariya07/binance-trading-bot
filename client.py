import os
from pathlib import Path

from dotenv import load_dotenv
from binance.client import Client

# Load .env
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")


client = Client(API_KEY, API_SECRET)

# Binance Futures Testnet
client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

# Sync with Binance server time
client.timestamp_offset = client.get_server_time()["serverTime"] - int(__import__("time").time() * 1000)