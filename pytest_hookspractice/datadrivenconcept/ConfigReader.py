import configparser
import os

config = configparser.RawConfigParser()

# ALWAYS point relative to THIS file (works in GitHub + Jenkins + local)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(BASE_DIR, "Config.ini")

files_loaded = config.read(config_path)

if not files_loaded:
    raise FileNotFoundError(f"Config.ini not found at {config_path}")


def get_application_url():
    return config.get("common info", "baseURL")


def get_browser():
    return config.get("common info", "browser")


def get_username():
    return config.get("login data", "username")


def get_password():
    return config.get("login data", "password")


def get_invalidusername():
    return config.get("login invaliddata", "username")


def get_invalidpassword():
    return config.get("login invaliddata", "password")