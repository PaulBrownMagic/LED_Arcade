#!/usr/bin/python3
import xml.etree.ElementTree as ET

CONFIG_FILE = "config.xml"
CONFIG_INPUT = "input"
CONFIG_DISPLAY = "display"
INPUTS = {"name": "input method", 1: "Keyboard", 2: "SenseHat"}
DISPLAYS = {"name": "display method", 1: "UnicornHat", 2: "SenseHat"}


def read_config():
    """Read in configuration from config.xml"""
    tree = ET.parse(CONFIG_FILE)
    return {child.tag: child.text for child in tree.getroot()}


def give_choice(options):
    print("Set {}".format(options["name"]))
    for num, name in options.items():
        if isinstance(num, int):
            print("{}: {}".format(num, name))
    choice = None
    while choice not in range(1, len(options) + 1):
        choice = int(input("Choose number: "))
    return options[choice]


def update_config():
    """Update config.xml"""
    print("Updating config")
    tree = ET.parse(CONFIG_FILE)
    root = tree.getroot()
    root.find(CONFIG_INPUT).text = give_choice(INPUTS)
    root.find(CONFIG_DISPLAY).text = give_choice(DISPLAYS)
    tree.write(CONFIG_FILE)
    print("Config Updated")


if __name__ == "__main__":
    update_config()
    print("Chosen configuration:")
    for k, v in read_config().items():
        print("{}: {}".format(k, v))
