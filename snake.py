from constants import COLOURS
from constants import WHITE
import numpy as np
import random

class Snake():
    """The player character, a snake that runs around eating food"""

    # Movement look-up values
    movements = {"up": (-1, 0),
                 "down": (1, 0),
                 "left": (0, -1),
                 "right": (0, 1)}
    horizontal = ["left", "right"]
    vertical = ["up", "down"]

    def __init__(self):
        self.body_list = [[2,1],[2,2]]  # starting location
        self.change_x = 1
        self.change_y = 0
        self.eaten = False  # Used to inform the food it has been eaten
        self.last_direction = None  # Used to prevent the snake turning 180

    def move(self, direction):
        """Update change_x and change_y values based on direction"""
        # Don't allow the snake to turn back on itself (180)
        if direction in self.horizontal and self.last_direction in self.horizontal:
            pass
        elif direction in self.vertical and self.last_direction in self.vertical:
            pass
        else:
            self.last_direction = direction
            try:
                self.change_x, self.change_y = self.movements[direction]
            except KeyError:  # Unknown input, doesn't matter what
                pass

    def update(self, food):
        """Actually move the snake, eat food, grow or not"""
        # Calculate new position
        new_x = self.body_list[0][0] + self.change_x
        new_y = self.body_list[0][1] + self.change_y
        # Boundary check
        new_x = 0 if new_x > 7 else new_x
        new_x = 7 if new_x < 0 else new_x
        new_y = 0 if new_y > 7 else new_y
        new_y = 7 if new_y < 0 else new_y
        # Make new segmant
        new_segmant = [new_x, new_y]
        self.body_list.insert(0, new_segmant)
        # Check for eating
        if new_segmant != food.pos:
            #Not eating, so can remove old segmant
            self.body_list.pop()
            self.eaten = False
        else:
            self.eaten = True

    def game_over(self):
        """See if the snake is eating itself"""
        if self.body_list[0] in self.body_list[1:]:
            return True
        return False


class Food():
    """The little things snakes eat"""

    def __init__(self):
        self.eaten = True #set to true so that it is reset at start
        self.pos = None
        self.colour = COLOURS[0]

    def update(self, snake):
        """ Re-make the food if it has been eaten """
        if self.eaten:
            #inside checks to ensure food isn't draw in the same location as the snakes body
            inside = True
            while inside:
                self.pos = [random.randint(0,7), random.randint(0,7)]
                if self.pos not in snake.body_list:
                    inside = False
            #give food a random colour from list of colours. List ensures visible strong colours
            self.colour = random.choice(COLOURS)
        self.eaten = False

#game class
class Game(object):

    def __init__(self):
        self.snake = None
        self.food = None
        self.game_over = False
        self.score = 0
        self.start = True  # Stop the game running immediately
        self.grid = None

    def run_logic(self, events):
        # check for game over first
        if self.snake:
            self.game_over = self.snake.game_over()
        # If it is game_over or the first game, wait for an event before starting
        if self.game_over or self.start:
            if len(events) > 0:
                self.snake = Snake()
                self.food = Food()
                self.start = False
                self.game_over = False
        # If the game is in progress, update!
        if not self.game_over and not self.start:
            # Update food
            self.food.update(self.snake)
            # Update snake
            for event in events:
                self.snake.move(event)
            self.snake.update(self.food)
            # See if the snake has eaten the food
            self.food.eaten = self.snake.eaten
            if self.food.eaten:
                self.score += 1

    def update_display(self):
        self.grid = np.zeros([8, 8, 3], dtype=int)
        if not self.start and not self.game_over:
            self.grid[self.food.pos[0], self.food.pos[1]] = self.food.colour
            for segmant in self.snake.body_list:
                self.grid[segmant[0], segmant[1]] = WHITE
        return self.grid
