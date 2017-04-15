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

NAV_SCREENS = {
"Snake": np.array([[m, w, m, m, m, m, w, m],
                   [w, m, m, m, m, m, m, w],
                   [m, w, m, m, m, m, w, m],
                   [m, m, g, g, g, g, m, m],
                   [m, m, g, m, m, m, r, m],
                   [m, m, g, g, g, g, m, m],
                   [m, m, m, m, m, g, m, m],
                   [m, m, g, g, g, g, m, m]]),
"Purple Rain": np.array([[n, w, n, n, n, n, w, n],
                         [w, n, n, p, n, n, n, w],
                         [n, w, n, n, p, n, w, n],
                         [n, p, n, n, n, n, n, n],
                         [n, n, p, n, p, p, n, n],
                         [p, n, n, n, n, p, n, n],
                         [n, n, n, n, n, n, n, p],
                         [p, n, n, n, g, n, n, n]]),
}