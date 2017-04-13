#!/usr/bin/python3
import unicornhat as unicorn
from sense_hat import SenseHat


class UnicornDisplay:
    """Unicorn Hat from Pimoroni, requires their library"""

    def __init__(self):
        unicorn.set_layout(unicorn.HAT)
        unicorn.rotation(180)
        unicorn.brightness(0.5)
        self.width, self.height = unicorn.get_shape()

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
