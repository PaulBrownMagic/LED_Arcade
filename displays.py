#!/usr/bin/python3
from sense_hat import SenseHat
import time
import unicornhat as unicorn
from writer import Writer


class UnicornDisplay:
    """Unicorn Hat from Pimoroni, requires their library"""

    def __init__(self):
        unicorn.set_layout(unicorn.HAT)
        unicorn.rotation(180)
        unicorn.brightness(0.5)
        self.width, self.height = unicorn.get_shape()
        self.writer = Writer()

    def show_message(self, phrase, scroll_speed=0.2, text_color=[255, 255, 255], background_color=[0, 0, 0]):
        self.writer.make_phrase(phrase)
        for frame in self.writer.generate_frames():
            grid = np.dstack([frame * text_color[0], frame * text_color[1], frame * text_color[2]])
            self.update(grid)
            time.sleep(scroll_speed)

    def update(self, grid):
        unicorn.set_pixels(grid.tolist())
        unicorn.show()

class SenseHatDisplay:
    """Official SenseHat"""

    def __init__(self):
        self.sense_hat = SenseHat()
        self.sense_hat.set_rotation(0)

    def update(self, grid):
        self.sense_hat.set_pixels(grid.reshape([64, 3]).tolist())

    def show_message(self, phrase, **kwargs):
        self.sense_hat.show_message(phrase, **kwargs)


if __name__ == "__main__":
    import numpy as np
    import time
    grid = np.zeros([8, 8, 3])
    display = UnicornDisplay()
    for _ in range(20):
        grid += 10
        display.update(grid)
        time.sleep(0.5)
    display.update(np.zeros([8, 8, 3]))
