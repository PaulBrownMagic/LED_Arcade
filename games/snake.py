from games.constants import WHITE, GREEN, DARK_RED, SNAKE_COLOURS
from games.constants import HORIZONTAL, VERTICAL
from games import Sprite
import numpy as np
import random


class Snake(Sprite):
    """The player character, a snake that runs around eating food"""

    def __init__(self):
        super().__init__(movement_axis=[HORIZONTAL, VERTICAL], no_double_back=True)
        self.body_list = [[2,1],[2,2]]  # starting location
        self.change = [1, 0]  # For x and y

    def update(self, food):
        """Actually move the snake, eat food, grow or not"""
        # Calculate new position
        new_x = self.body_list[0][0] + self.change[0]
        new_y = self.body_list[0][1] + self.change[1]
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

    def game_over(self):
        """See if the snake is eating itself"""
        if self.body_list[0] in self.body_list[1:]:
            return True
        return False


class Food():
    """The little things snakes eat"""

    def __init__(self, snake):
        self.pos = None
        self.colour = None
        self.reset(snake)

    def reset(self, snake):
        """ Re-make the food if it has been eaten """
        #inside checks to ensure food isn't draw in the same location as the snakes body
        inside = True
        while inside:
            self.pos = [random.randint(0,7), random.randint(0,7)]
            if self.pos not in snake.body_list:
                inside = False
        #give food a random colour from list of colours. List ensures visible strong colours
        self.colour = random.choice(SNAKE_COLOURS)


class Game:
    fps = 0.1

    def __init__(self):
        self.snake = Snake()
        self.food = Food(self.snake)
        self.game_over = False
        self.score = 0

    def handle_events(self, events):
        for event in events:
            self.snake.move(event)

    def run_logic(self):
        # Check for game over first
        self.game_over = self.snake.game_over()
        # Update snake
        self.snake.update(self.food)
        # See if the snake has eaten the food
        if self.snake.body_list[0] == self.food.pos:
            self.food.reset(self.snake)
            self.score += 1

    def update_display(self):
        grid = np.empty([8, 8, 3], dtype=int)
        grid[:, :, :] = DARK_RED
        if self.food and self.snake:
            grid[self.food.pos[0], self.food.pos[1]] = self.food.colour
            for segmant in self.snake.body_list:
                grid[segmant[0], segmant[1]] = GREEN
        return grid
