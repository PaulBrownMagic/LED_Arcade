from displays.display import Display

from config import read_config


def load_display():
    config_display = read_config()['display']
    if config_display == "SenseHat":
        from displays.sensehat_display import SenseHatDisplay
        return SenseHatDisplay()
    elif config_display == "UnicornHat":
        from displays.unicorn_display import UnicornDisplay
        return UnicornDisplay()
