from games.assets.sprite import Sprite, Co_ordinates
from games import snake, purple_rain, pacman


def load_game(name):
    if name == "Snake":
        return snake.Game()
    elif name == "Purple Rain":
        return purple_rain.Game()
    elif name == "Pacman":
        return pacman.Game()
    else:
        raise KeyError("Unknown Game Selected")
