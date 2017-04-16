
from games.constants import HORIZONTAL
from games.constants import GREEN, YELLOW, RED, PURPLE, DARK_BLUE
from games import Sprite
import numpy as np
import random
import time


class Player(Sprite):
    """ Pixel that'll be controlled by the player """

    def __init__(self):
        super().__init__([HORIZONTAL])
        self.position = [7,3]  # starting location
        self.change = 0  # x-axis
        self.colour = GREEN

    def update(self,lives):
        # update paddle to new position
        self.position[1] += self.change
        self.change = 0  # stop moving when no input
        # check_boundaries
        self.position[1] = 0 if self.position[1] < 0 else self.position[1]
        self.position[1] = 7 if self.position[1] > 7 else self.position[1]
        if lives == 2:
            self.colour = YELLOW
        elif lives == 1:
            self.colour = RED


class Rain():

    def __init__(self):
        self.position = [random.randint(-20,-1), random.randint(0,7)]
        self.change = 0.5  # y-axis
        self.display = False
        self.int_pos = None

    def update(self,paddle):
        # reset to top if off screen
        if self.position[0] == 7:
            self.position = [random.randint(-20,-1), random.randint(0,7)]
            self.display = False
            self.int_pos = None
        # set new position and display
        self.position[0]+= self.change
        # Adjust for easy display if in grid
        if self.position[0] >= 0  and self.position[0]%1==0:
            self.display = True
            self.int_pos = [int(self.position[0]),int(self.position[1])]


class Game:
    fps = 1/12

    def __init__(self):
        self.lives = 3
        self.player = Player()
        self.game_over = False
        self.rain = [Rain() for _ in range(20)]

    def handle_events(self, events):
        # All events processed, last valid action taken
        for event in events:
            self.player.move(event)


    def run_logic(self):
        #check for game over first
        if self.lives <= 0:
            self.game_over = True
        # Update sprites
        self.player.update(self.lives)
        for r in self.rain:
            r.update(self.player.position)
            if r.int_pos == self.player.position:
                self.lives -= 1

    def update_display(self):
        grid = np.empty([8, 8, 3], dtype=int)
        grid[:, :, :] = DARK_BLUE
        if self.rain and self.player:
            grid[self.player.position[0], self.player.position[1]] = self.player.colour
            for r in self.rain:
                if r.display:
                    grid[r.int_pos[0], r.int_pos[1]] = PURPLE
        return grid
