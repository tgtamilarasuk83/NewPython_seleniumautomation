from configparser import ConfigParser

def config_Read(category, key):
    config = ConfigParser()

    config.read(
        r"D:\9-6-16 pytest practice\TutorialsNinja\DataProviders\config.ini"
    )

    return config.get(category, key)