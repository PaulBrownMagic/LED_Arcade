
import random

import numpy as np

from games import Sprite
from games.constants import (DARK_BLUE, GREEN, HORIZONTAL, PURPLE, RED,
                             VERTICAL, YELLOW)


class Player(Sprite):
    """ Pixel that'll be controlled by the player """

    def __init__(self):
        super().__init__([HORIZONTAL])
        self.position.set([3, 7])  # starting location
        self.change = 0   # x-axis
        self.colour = GREEN

    def update(self, lives):
        # update paddle to new position
        self.update_position()
        self.change = 0  # stop moving when no input
        if lives == 2:
            self.colour = YELLOW
        elif lives == 1:
            self.colour = RED


class Rain(Sprite):
    """ Purple pixels that fall from the sky, uses own movement logic"""

    def __init__(self):
        super().__init__(movement_axis=None)  # movement_axis not applicable
        # abstract_position off display as an easy way to randomise timing
        self.abstract_position = {"x": random.randint(0, 7),
                                  "y": random.randint(-20, -1)}
        self.change = 0.5  # y-axis, half-pixel updates for movement every 2 frames
        self.display = False  # Can't display it when off display

    def update(self, paddle):
        # update abstract_position
        self.abstract_position["y"] += self.change
        # reset to top if off bottom of display
        if self.abstract_position["y"] >= 8:  # int(7.5) = 7
            self.abstract_position["x"] = random.randint(0, 7)
            self.abstract_position["y"] = random.randint(-20, -1)
            self.display = False
            self.position.set([None, None])  # Avoid collision with player
        # If within display, set the variables required
        if 0 <= int(self.abstract_position["y"]) < 8:
            self.display = True
            self.position.set([self.abstract_position["x"],
                               self.abstract_position["y"]])  # Forced to int by set()


class Game:
    fps = 1 / 12

    def __init__(self):
        self.lives = 3
        self.player = Player()
        self.game_over = False
        self.rain = [Rain() for _ in range(20)]

    def process_events(self, events):
        # All events processed, last valid action taken
        for event in events:
            self.player.event_response(event)

    def run_logic(self):
        # check for game over first
        if self.lives <= 0:
            self.game_over = True
        # Update sprites
        self.player.update(self.lives)
        for r in self.rain:
            r.update(self.player.position)
            if r.position == self.player.position:
                self.lives -= 1

    def update_display(self):
        # Make background
        grid = np.empty([8, 8, 3], dtype=int)
        grid[:, :, :] = DARK_BLUE
        # Add player and rain
        grid[self.player.position.y, self.player.position.x] = self.player.colour
        for r in self.rain:
            if r.display:  # grid[None, None] is whole grid!
                grid[r.position.y, r.position.x] = PURPLE
        return grid
