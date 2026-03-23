import os
from dotenv import load_dotenv


load_dotenv()


BASE_URL = os.getenv("BASE_URL")
DEFAULT_USER_EMAIL = os.getenv("DEFAULT_USER_EMAIL")
DEFAULT_USER_PASSWORD = os.getenv("DEFAULT_USER_PASSWORD")

