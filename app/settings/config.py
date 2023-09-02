import os
from dotenv import dotenv_values

def get_env(is_local, dir):
    return dotenv_values(os.path.join(dir, ".env")) if is_local else os.environ

class Settings:
    # Basic Application Information
    VERSION = '0.2.0'
    APP_TITLE = 'Google App Engine'
    PROJECT_NAME = 'Google App Engine'
    APP_DESCRIPTION = 'Google App Engine Python FastAPI service'
    CONTACT = {
        "name": "Arkadip Bhattacharya",
        "email": "hi@arkadip.dev",
    }

    # Running Type
    DEBUG = os.getenv("ENV") != "PROD"
    LOCAL = os.getenv("ENV") not in ["PROD", "TEST"]

    ROOT_PATH = ""

    # Directory information
    PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    BASE_DIR = os.path.abspath(os.path.join(PROJECT_ROOT, os.pardir))
    LOGS_ROOT = os.path.join(PROJECT_ROOT, "logs")

    env = get_env(LOCAL, BASE_DIR)

    # Route Information
    API_V1_STR = "/"

    CORS_ORIGINS = [
        "http://localhost",
        "http://localhost:8080",
        "http://localhost:5000",
        "http://localhost:3000",
    ]
    CORS_ALLOW_CREDENTIALS = True
    CORS_ALLOW_METHODS = ["*"]
    CORS_ALLOW_HEADERS = ["*"]

settings = Settings()