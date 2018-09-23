import os
import toml

CONFIG_DIR = os.path.expanduser("~/.local/share/screen-time/")
CONFIG_FILE = "config.toml"

DEFAULT_CONFIG = {
    'goals': {
        'break_points': 48,
        'screen_off_points': 64
    }
}


def create_default_config():
    if not os.path.exists(CONFIG_DIR):
        os.mkdir(CONFIG_DIR)
    write_config(DEFAULT_CONFIG)


def read_config():
    if os.path.exists(os.path.join(CONFIG_DIR, CONFIG_FILE)):
        f = open(os.path.join(CONFIG_DIR, CONFIG_FILE), "r")
        return toml.load(f, _dict=dict)
    else:
        create_default_config()
        return DEFAULT_CONFIG


def write_config(configuraton_obj):
    if not os.path.exists(CONFIG_DIR):
        os.mkdir(CONFIG_DIR)
    f = open(os.path.join(CONFIG_DIR, CONFIG_FILE), "w")
    toml.dump(configuraton_obj, f)
