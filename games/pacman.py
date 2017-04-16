from random import randint, randrange, choice
import random
from games import Sprite
from games.assets import pacman_mazes as mazes
from games.constants import *
import time


class Maze():

    def __init__(self):
        self.maze_number = 0
        self.grid = mazes.MAZES[self.maze_number]
        self.number_of_mazes = len(mazes.MAZES) - 1

    def update(self, pacman):
        self.grid[pacman[1], pacman[0]] = BLACK
        return self.grid

    def next_level(self):
        self.maze_number += 1
        self.maze_number = 0 if self.maze_number > self.number_of_mazes else self.maze_number
        self.grid = mazes.MAZES[self.maze_number]

class Pacman(Sprite):
    """Pacman the player"""

    def __init__(self):
        super().__init__([HORIZONTAL, VERTICAL])
        self.change = [0, 0]
        self.position = [3,4]

    def reset(self):
        self.change = [0, 0]
        self.position = [3,4]

    def update(self,grid):
        # Calculate new position
        new_x = self.position[0] + self.change[0]
        new_y = self.position[1] + self.change[1]
        # Boundary check
        new_x = 0 if new_x > 7 else new_x
        new_x = 7 if new_x < 0 else new_x
        new_y = 0 if new_y > 7 else new_y
        new_y = 7 if new_y < 0 else new_y
        # Grid check
        if not all(grid[new_x, new_y] == BLUE):
            self.position = [new_x, new_y]

"""
class Ghost():
    #attributes
    direction = None
    position = None
    ai_left = None
    ai_right = None
    ai_forward = None
    mode = None
    target = None
    colour = None
    #Methods
    def __init__(self,colour,target_offset,start_offset):
        self.position = [3+start_offset,0]
        self.direction = choice(['r','l'])
        self.mode = 'chase'
        self.target_offset = target_offset
        self.colour = colour
    def reset(self,offset):
        self.position = [3+offset,0]
        self.direction = choice(['r','l'])
    def update(self,pacman,grid):
        move = self.direction
        #move
        if move == 'r' and self.position[0]<7:
            self.position[0]+=1
            self.ai_left = [self.position[0],self.position[1]-1]
            self.ai_right = [self.position[0],self.position[1]+1]
            self.ai_forward = [self.position[0]+1,self.position[1]]
        elif move == 'l' and self.position[0]>0:
            self.position[0]-=1
            self.ai_left = [self.position[0],self.position[1]+1]
            self.ai_right = [self.position[0],self.position[1]-1]
            self.ai_forward = [self.position[0]-1,self.position[1]]
        elif move == 'u'and self.position[1]>0:
            self.position[1]-=1
            self.ai_left = [self.position[0]-1,self.position[1]]
            self.ai_right = [self.position[0]+1,self.position[1]]
            self.ai_forward = [self.position[0],self.position[1]-1]
        elif move == 'd' and self.position[1]<7:
            self.position[1]+=1
            self.ai_left = [self.position[0]+1,self.position[1]]
            self.ai_right = [self.position[0]-1,self.position[1]]
            self.ai_forward = [self.position[0],self.position[1]+1]
        unicorn.set_pixel(self.position[0],self.position[1],self.colour[0],self.colour[1],self.colour[2])
        #choose target
        target = [2 + self.target_offset, 2]
        if self.mode == 'chase':
            if pacman.direction == 'r':
                target = [pacman.position[0]+self.target_offset,pacman.position[1]]
            elif pacman.direction == 'l':
                target = [pacman.position[0]-self.target_offset,pacman.position[1]]
            elif pacman.direction == 'u':
                target = [pacman.position[0],pacman.position[1]-self.target_offset]
            elif pacman.direction == 'd':
                target = [pacman.position[0],pacman.position[1]+self.target_offset]
        #choose direction
        l_dist = 200
        r_dist = 200
        f_dist = 200
        try:
            if grid[self.ai_left[1]][self.ai_left[0]] != 'b':
                x_len = self.ai_left[0]-target[0]
                y_len = self.ai_left[1]-target[1]
                l_dist =  x_len**2 + y_len**2
        except:
            pass
        try:
            if grid[self.ai_right[1]][self.ai_right[0]] != 'b':
                x_len = self.ai_right[0]-target[0]
                y_len = self.ai_right[1]-target[1]
                r_dist =  x_len**2 + y_len**2
        except:
            pass
        try:
            if grid[self.ai_forward[1]][self.ai_forward[0]] != 'b':
                x_len = self.ai_forward[0]-target[0]
                y_len = self.ai_forward[1]-target[1]
                f_dist =  x_len**2 + y_len**2
        except:
            pass
        shortest = min(l_dist,r_dist,f_dist)
        directions = ['u','r','d','l']
        if shortest == l_dist:
            if self.direction == directions[0]:
                self.direction = directions[3]
            else:
                self.direction = directions[directions.index(self.direction)-1]
        elif shortest == r_dist:
            if self.direction == directions[3]:
                self.direction = directions[0]
            else:
                self.direction = directions[directions.index(self.direction)+1]
        else:
            self.direction = move
"""

class Game(object):
    fps = 1/8

    def __init__(self):
        self.lives = 3
        self.level = 0
        self.score = 0
        self.maze = Maze()
        self.pacman = Pacman()
        #self.blinky = Ghost(RED,0,0)
        #self.inky = Ghost(PURPLE,4,1)
        self.game_over = False
        self.frame = 0
        time.sleep(1)

    def handle_events(self, events):
        for event in events:
            self.pacman.move(event)

    def run_logic(self):
        #check for game over first
        if self.lives == 0:
            self.game_over = True
        #only if it is not the first game and not game over update the food and snake
        self.maze.update(self.pacman.position)
        """
            if self.pacman.position == self.blinky.position or self.pacman.position == self.inky.position:
                self.lives -= 1
                self.pacman.reset()
                self.blinky.reset(0)
                self.inky.reset(1)
                time.sleep(1)
        """
        self.pacman.update(self.maze.grid)
        if all(self.maze.grid[self.pacman.position[0], self.pacman.position[1]] == ORANGE):
            self.score += 1
        #self.blinky.update(self.pacman,self.maze.grid)
        #self.inky.update(self.pacman,self.maze.grid)
        #self.frame+=1
        #if self.frame == 50:
        #    self.blinky.mode = 'scatter'
        #    self.inky.mode = 'scatter'
        #if self.frame == 70:
        #    self.blinky.mode = 'chase'
        #    self.inky.mode = 'chase'
        #    self.frame = 0
        if ORANGE not in self.maze.grid:
            self.lives+=1
            self.maze.next_level()
            self.pacman.reset()
            #self.blinky.reset(0)
            #self.inky.reset(1)
            time.sleep(1)

    def update_display(self):
        grid = self.maze.grid.copy()
        grid[self.pacman.position[0], self.pacman.position[1]] = YELLOW
        return grid
