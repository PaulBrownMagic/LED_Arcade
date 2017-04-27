import random
import time
from random import choice, randint, randrange

from games import Sprite
from games.assets import pacman_mazes as mazes
from games.constants import *
from inputs import DOWN, LEFT, RIGHT, UP


class Maze():
    """Load and display mazes for levels"""

    def __init__(self):
        self.maze_number = 0
        self.grid = mazes.MAZES[self.maze_number].copy()
        self.number_of_mazes = len(mazes.MAZES) - 1

    def update(self, pacman_position):
        self.grid[pacman_position.y, pacman_position.x] = BLACK
        return self.grid

    def next_level(self):
        self.maze_number += 1
        # Cycle mazes
        self.maze_number = 0 if self.maze_number > self.number_of_mazes else self.maze_number
        self.grid = mazes.MAZES[self.maze_number].copy()


class Pacman(Sprite):
    """Pacman the player"""

    def __init__(self):
        super().__init__([HORIZONTAL, VERTICAL])
        self.position.set([3, 4])

    def reset(self):
        """Go back to start position"""
        self.change = [0, 0]  # Stop moving
        self.position.set([3, 4])

    def update(self, grid):
        new_x, new_y = self.move()
        # Grid check
        if not all(grid[new_y, new_x] == BLUE):
            self.position.x, self.position.y = new_x, new_y


class Ghost(Sprite):
    """Blinky and Inky with AI to chase Pacman"""
    count = 0
    horizontal = list(HORIZONTAL)
    vertical = list(VERTICAL)

    def __init__(self, colour, target_offset):
        # Ghosts don't double back, but logic implemented in update because AI
        super().__init__([HORIZONTAL, VERTICAL])
        self.position.set([3 + Ghost.count, 0])
        self.number = Ghost.count
        Ghost.count += 1
        self.number = self.count
        self.change = choice([[1, 0], [-1, 0]])
        self.opposite_direction = UP
        self.mode = 'chase'
        self.target_offset = target_offset
        self.colour = colour

    def reset(self):
        """Move back to start position"""
        self.position.set([3 + self.number, 0])
        self.change = choice([[1, 0], [-1, 0]])

    def get_distance(self, ai, target, grid):
        """Calculate euclidean distance squared, no need to sqrt it for this"""
        # Off the edge of the display
        if -1 in ai or 8 in ai:
            return 255
        # Check it's not blue, if it is then direction is invalid
        if not all(grid[ai[1], ai[0]] == BLUE):
            x_len = ai[0] - target[0]
            y_len = ai[1] - target[1]
            return x_len**2 + y_len**2
        # Invalid direction, max distance is 98, so 255 can't be picked.
        else:
            return 255

    def get_target_position(self, pacman):
        """Calculate where ghost is trying to get"""
        target = [2 + self.target_offset, 2]  # Go to two top corners, not chase
        if self.mode == 'chase':
            # How far the target is from pacman with direction
            target_change = [pacman.change[0] * self.target_offset,
                             pacman.change[1] * self.target_offset]
            # Convert to co-ordinates
            target = [pacman.position[0] + target_change[0],
                      pacman.position[1] + target_change[1]]
        return target

    def update(self, pacman, grid):
        # Positions of AI measurement locations
        ai_locations = {UP:  [self.position.x,
                              self.position.y - 1],
                        DOWN: [self.position.x,
                               self.position.y + 1],
                        LEFT: [self.position.x - 1,
                               self.position.y],
                        RIGHT: [self.position.x + 1,
                                self.position.y]
                        }
        # choose target
        target = self.get_target_position(pacman)
        # choose direction
        distances = {direction: self.get_distance(ai, target, grid)
                     for direction, ai in ai_locations.items()
                     if direction != self.opposite_direction}
        direction = min(distances, key=distances.get)
        self.event_response(direction)
        # update opposite direction
        if direction in self.horizontal:
            self.opposite_direction = self.horizontal[1 - self.horizontal.index(direction)]
        elif direction in self.vertical:
            self.opposite_direction = self.vertical[1 - self.vertical.index(direction)]
        # Calculate new position
        new_x, new_y = self.move()
        # Grid check
        if not all(grid[new_y, new_x] == BLUE):
            self.position.x, self.position.y = new_x, new_y


class Game(object):
    fps = 1 / 3  # Keep it slow!

    def __init__(self):
        self.lives = 3
        self.level = 0
        self.score = 0
        self.maze = Maze()
        self.pacman = Pacman()
        self.blinky = Ghost(RED, 0)
        self.inky = Ghost(PURPLE, 4)
        self.game_over = False
        self.frame = 0
        time.sleep(1)

    def reset_sprites(self):
        self.pacman.reset()
        self.blinky.reset()
        self.inky.reset()

    def process_events(self, events):
        for event in events:
            self.pacman.event_response(event)

    def run_logic(self):
        # check for game over first
        if self.lives == 0:
            self.game_over = True
            return

        # check if pacman has been caught
        if self.pacman.position == self.blinky.position or self.pacman.position == self.inky.position:
            self.lives -= 1
            self.reset_sprites()
            time.sleep(1)

        # see if pacman is eating an orange
        if all(self.maze.grid[self.pacman.position.y, self.pacman.position.x] == ORANGE):
            self.score += 1

        # update maze
        self.maze.update(self.pacman.position)

        # update pacman
        self.pacman.update(self.maze.grid)

        # update ghosts
        self.blinky.update(self.pacman, self.maze.grid)
        self.inky.update(self.pacman, self.maze.grid)
        # update ghost mode
        self.frame += 1
        if self.frame == 50:
            self.blinky.mode = 'scatter'
            self.inky.mode = 'scatter'
        if self.frame == 70:
            self.blinky.mode = 'chase'
            self.inky.mode = 'chase'
            self.frame = 0

        # check if the maze is finished
        if ORANGE not in self.maze.grid:
            self.lives += 1
            self.maze.next_level()
            self.reset_sprites()
            time.sleep(1)

    def update_display(self):
        # Copy grid to not update original
        grid = self.maze.grid.copy()
        # Put pacman on
        grid[self.pacman.position.y, self.pacman.position.x] = YELLOW
        # Put ghosts on
        grid[self.blinky.position.y, self.blinky.position.x] = self.blinky.colour
        grid[self.inky.position.y, self.inky.position.x] = self.inky.colour
        return grid
