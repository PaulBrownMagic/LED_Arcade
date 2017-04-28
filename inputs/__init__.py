from config import read_config


def load_controller():
    config_input = read_config()['input']
    if config_input == "SenseHat":
        from inputs.sensehat_input import SenseHatInput
        return SenseHatInput()
    elif config_input == "Keyboard":
        from inputs.keyboard import KeyboardInput
        return KeyboardInput()


# constants
LEFT = "left"
RIGHT = "right"
UP = "up"
DOWN = "down"
BUTTON = "middle"
