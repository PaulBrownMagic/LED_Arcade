from inputs import DOWN, LEFT, RIGHT, UP

# colours       r    g    b
BLACK = (0,   0,   0)
WHITE = (255, 255, 255)
GREEN = (0, 255,   0)
RED = (255,   0,   0)
BLUE = (0,   0, 255)
DARK_BLUE = (0,   0,  50)
YELLOW = (255, 255,   0)
PURPLE = (255,   0, 255)
ORANGE = (150, 105,  20)
CYAN = (0, 255, 255)
DARK_RED = (50,   0,   0)
SNAKE_COLOURS = (WHITE, ORANGE, YELLOW, PURPLE, CYAN, BLUE)

# Movement axis and changes
VERTICAL = {UP: (0, -1),
            DOWN: (0, 1)}
HORIZONTAL = {LEFT: (-1, 0),
              RIGHT: (1, 0)}
