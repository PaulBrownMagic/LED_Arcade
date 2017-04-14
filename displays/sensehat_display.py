from displays import Display
from sense_hat import SenseHat


class SenseHatDisplay(Display):
    """Official SenseHat"""

    def __init__(self):
        self.sense_hat = SenseHat()
        self.sense_hat.set_rotation(0)

    def update(self, grid):
        self.sense_hat.set_pixels(grid.reshape([64, 3]).tolist())

    def show_message(self, phrase, scroll_speed=0.1, text_color=[255, 255, 255], background_color=[0, 0, 0]):
        self.sense_hat.show_message(phrase, scroll_speed, text_color, background_color)
