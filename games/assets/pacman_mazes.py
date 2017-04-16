from games.constants import ORANGE, BLACK, BLUE
import numpy as np
"""----------------------------
Mazes for pacman
-------------------------------"""
o = ORANGE
b= BLUE
k= BLACK

maze1 = np.array([[o, o, o, k, k, o, o, o],
                  [o, b, o, b, b, o, b, o],
                  [o, b, o, o, o, o, b, o],
                  [o, b, o, b, b, o, b, o],
                  [o, o, o, k, k, o, o, o],
                  [o, b, o, b, b, o, b, o],
                  [o, b, o, o, o, o, b, o],
                  [o, o, o, b, b, o, o, o]
                  ], dtype=int)

maze2 = np.array([[b, b, o, k, k, o, b, b],
                  [o, o, o, b, b, o, o, o],
                  [o, b, o, o, o, o, b, o],
                  [o, b, b, o, o, b, b, o],
                  [o, o, o, k, k, o, o, o],
                  [o, b, b, o, o, b, b, o],
                  [o, o, b, o, o, b, o, o],
                  [b, o, o, o, o, o, o, b]
                  ], dtype=int)

maze3 = np.array([[o, o, o, k, k, o, o, o],
                  [o, b, o, b, b, o, b, o],
                  [o, o, o, o, o, o, o, o],
                  [b, b, o, b, b, o, b, b],
                  [o, o, o, k, k, o, o, o],
                  [o, b, o, b, b, o, b, o],
                  [o, b, o, b, b, o, b, o],
                  [o, o, o, o, o, o, o, o]
                  ], dtype=int)

maze4 = np.array([[b, b, o, k, k, o, b, b],
                  [o, o, o, b, b, o, o, o],
                  [o, b, o, b, b, o, b, o],
                  [o, o, o, o, o, o, o, o],
                  [o, b, o, k, k, o, b, o],
                  [o, b, b, o, o, b, b, o],
                  [o, o, b, o, o, b, o, o],
                  [b, o, o, o, o, o, o, b]
                  ], dtype=int)

MAZES = [maze1, maze2, maze3, maze4]
