import configparser


def get_configs():
    config = configparser.ConfigParser()
    config.read("config.ini")
    return config
