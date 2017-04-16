from games.constants import *
import numpy as np

k = BLACK
g = GREEN
w = WHITE
r = RED
b = BLUE
m = DARK_RED
n = DARK_BLUE
p = PURPLE
o = ORANGE
y = YELLOW

NAV_SCREENS = {
    "Snake":        np.array([[m, w, m, m, m, m, w, m],
                              [w, m, m, m, m, m, m, w],
                              [m, w, m, m, m, m, w, m],
                              [m, m, g, g, g, g, m, m],
                              [m, m, g, m, m, m, b, m],
                              [m, m, g, g, g, g, m, m],
                              [m, m, m, m, m, g, m, m],
                              [m, m, g, g, g, g, m, m]
                              ], dtype=int),
    "Purple Rain":  np.array([[n, w, n, n, n, n, w, n],
                              [w, n, n, p, n, n, n, w],
                              [n, w, n, n, p, n, w, n],
                              [n, p, n, n, n, n, n, n],
                              [n, n, p, n, p, p, n, n],
                              [p, n, n, n, n, p, n, n],
                              [n, n, n, n, n, n, n, p],
                              [p, n, n, n, g, n, n, n]
                              ], dtype=int),
    "Pacman":       np.array([[k, w, k, k, p, k, w, k],
                              [w, k, k, b, b, k, k, w],
                              [k, w, k, o, r, k, w, k],
                              [o, b, o, b, b, o, b, o],
                              [o, o, o, k, k, k, k, k],
                              [o, b, o, b, b, o, b, k],
                              [o, b, o, o, o, y, b, k],
                              [o, o, o, b, b, k, k, k]
                              ], dtype=int)
}
EXIT_SCREEN = {
"Exit":             np.array([[r, w, k, k, k, k, w, k],
                              [w, r, k, r, r, k, k, w],
                              [k, w, r, k, k, r, w, k],
                              [k, r, k, r, k, k, r, k],
                              [k, r, k, k, r, k, r, k],
                              [k, k, r, k, k, r, k, k],
                              [k, k, k, r, r, k, r, k],
                              [k, k, k, k, k, k, k, r]
                              ], dtype=int)
}
