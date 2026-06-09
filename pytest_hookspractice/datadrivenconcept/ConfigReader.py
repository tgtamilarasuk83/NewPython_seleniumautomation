import configparser

config = configparser.RawConfigParser()

config_path = "Config.ini"

files_loaded = config.read(config_path)
print("Loaded config files:", files_loaded)

if not files_loaded:
    raise FileNotFoundError("Config.ini not found")

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