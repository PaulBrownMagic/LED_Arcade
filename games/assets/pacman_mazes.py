from games.constants import *
import numpy as np
"""----------------------------
Mazes for pacman
-------------------------------"""
o = ORANGE
b= BLUE
n= BLACK

maze1 = np.array([ [ o, o, o, n, n, o, o, o],
                   [ o, b, o, b, b, o, b, o],
                   [ o, b, o, o, o, o, b, o],
                   [ o, b, o, b, b, o, b, o],
                   [ o, o, o, n, n, o, o, o],
                   [ o, b, o, b, b, o, b, o],
                   [ o, b, o, o, o, o, b, o],
                   [ o, o, o, b, b, o, o, o] ])

maze2 = np.array([ [ b, b, o, n, n, o, b, b],
                   [ o, o, o, b, b, o, o, o],
                   [ o, b, o, o, o, o, b, o],
                   [ o, b, b, o, o, b, b, o],
                   [ o, o, o, n, n, o, o, o],
                   [ o, b, b, o, o, b, b, o],
                   [ o, o, b, o, o, b, o, o],
                   [ b, o, o, o, o, o, o, b] ])

maze3 = np.array([ [ o, o, o, n, n, o, o, o],
                   [ o, b, o, b, b, o, b, o],
                   [ o, o, o, o, o, o, o, o],
                   [ b, b, o, b, b, o, b, b],
                   [ o, o, o, n, n, o, o, o],
                   [ o, b, o, b, b, o, b, o],
                   [ o, b, o, b, b, o, b, o],
                   [ o, o, o, o, o, o, o, o] ])

maze4 = np.array([ [ b, b, o, n, n, o, b, b],
                   [ o, o, o, b, b, o, o, o],
                   [ o, b, o, b, b, o, b, o],
                   [ o, o, o, o, o, o, o, o],
                   [ o, b, o, n, n, o, b, o],
                   [ o, b, b, o, o, b, b, o],
                   [ o, o, b, o, o, b, o, o],
                   [ b, o, o, o, o, o, o, b] ])

MAZES = [maze1, maze2, maze3, maze4]
