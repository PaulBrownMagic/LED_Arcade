import random

import numpy as np

from games import Co_ordinates, Sprite
from games.constants import (DARK_RED, GREEN, HORIZONTAL, SNAKE_COLOURS,
                             VERTICAL, WHITE)


class Snake(Sprite):
    """The player character, a snake that runs around eating food"""

    def __init__(self):
        super().__init__(
            movement_axis=[HORIZONTAL, VERTICAL], no_double_back=True, solid_boundaries=False)
        # starting location
        self.body_list = [Co_ordinates([2, 1]), Co_ordinates([2, 2])]
        self.change = [1, 0]  # For x and y

    def update(self, food):
        """Actually move the snake, eat food, grow or not"""
        # Make new segmant
        new_segmant = Co_ordinates(position=self.move(self.body_list[0]))
        self.body_list.insert(0, new_segmant)
        # Check for eating
        if new_segmant != food.position:
            # Not eating, so can remove old segmant
            self.body_list = self.body_list[:-1]

    def game_over(self):
        """See if the snake is eating itself"""
        if self.body_list[0] in self.body_list[1:]:
            return True
        return False


class Food(Sprite):
    """The little things snakes eat"""

    def __init__(self, snake):
        super().__init__(movement_axis=[None])  # Does not move
        self.colour = None
        self.reset(snake)

    def reset(self, snake):
        """ Re-make the food if it has been eaten """
        # inside checks to ensure food isn't draw in the same location as the snakes body
        inside = True
        while inside:
            self.position.set([random.randint(0, 7), random.randint(0, 7)])
            if self.position not in snake.body_list:
                inside = False
        # give food a random colour from list of colours. List ensures visible strong colours
        self.colour = random.choice(SNAKE_COLOURS)


class Game:
    fps = 1 / 8

    def __init__(self):
        self.snake = Snake()
        self.food = Food(self.snake)
        self.game_over = False
        self.score = 0

    def process_events(self, events):
        for event in events:
            self.snake.event_response(event)

    def run_logic(self):
        # Check for game over first
        self.game_over = self.snake.game_over()
        # Update snake
        self.snake.update(self.food)
        # See if the snake has eaten the food
        if self.snake.body_list[0] == self.food.position:
            self.food.reset(self.snake)
            self.score += 1

    def update_display(self):
        # Make background
        grid = np.empty([8, 8, 3], dtype=int)
        grid[:, :, :] = DARK_RED
        # Add Food and Snake
        grid[self.food.position.y, self.food.position.x] = self.food.colour
        for segmant in self.snake.body_list:
            grid[segmant.y, segmant.x] = GREEN
        return grid
