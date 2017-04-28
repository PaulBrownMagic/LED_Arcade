import time

import numpy as np

from displays.writer import Writer


class Display:
    """Default methods for all displays"""

    def __init__(self):
        self.writer = Writer()

    def update(self, grid):
        """Must be overwritten by subclasses with appropriate method"""
        pass

    def clear(self):
        """Turn all pixels off"""
        self.update(np.zeros([8, 8, 3], dtype=int))

    def show_message(self, phrase, scroll_speed=0.2, text_color=[255, 255, 255], background_color=[0, 0, 0]):
        """Display a scrolling message"""
        self.writer.make_phrase(phrase)
        for frame in self.writer.generate_frames():
            grid = np.dstack([frame * text_color[0], frame * text_color[1], frame * text_color[2]])
            if background_color != [0, 0, 0]:
                # Requires numpy>=1.12.1 to work
                np.place(grid, grid == [0, 0, 0], background_color)
            self.update(grid)
            time.sleep(scroll_speed)
