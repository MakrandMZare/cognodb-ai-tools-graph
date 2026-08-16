from dotenv import load_dotenv
import os

load_dotenv()

CONGODB_URI = os.getenv("CONGODB_URI")
CONGODB_USER = os.getenv("CONGODB_USER")
CONGODB_PASSWORD = os.getenv("CONGODB_PASSWORD")