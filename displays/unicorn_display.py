import unicornhat as unicorn
from displays import Display


class UnicornDisplay(Display):
    """Unicorn Hat from Pimoroni, requires their library"""

    def __init__(self):
        super().__init__()
        unicorn.set_layout(unicorn.HAT)
        unicorn.rotation(180)
        unicorn.brightness(0.5)
        self.width, self.height = unicorn.get_shape()

    def update(self, grid):
        unicorn.set_pixels(grid.tolist())
        unicorn.show()
