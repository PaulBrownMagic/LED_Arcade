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
"Snake": np.array([[m, w, m, m, m, m, w, m],
                   [w, m, m, m, m, m, m, w],
                   [m, w, m, m, m, m, w, m],
                   [m, m, g, g, g, g, m, m],
                   [m, m, g, m, m, m, b, m],
                   [m, m, g, g, g, g, m, m],
                   [m, m, m, m, m, g, m, m],
                   [m, m, g, g, g, g, m, m]
                   ]),
"Purple Rain": np.array([[n, w, n, n, n, n, w, n],
                         [w, n, n, p, n, n, n, w],
                         [n, w, n, n, p, n, w, n],
                         [n, p, n, n, n, n, n, n],
                         [n, n, p, n, p, p, n, n],
                         [p, n, n, n, n, p, n, n],
                         [n, n, n, n, n, n, n, p],
                         [p, n, n, n, g, n, n, n]
                         ]),
"Pacman": np.array([ [ o, w, o, k, k, o, w, o],
                     [ w, b, o, r, b, o, b, w],
                     [ o, w, o, o, o, o, w, o],
                     [ o, b, o, b, b, o, b, o],
                     [ o, o, o, y, k, o, o, o],
                     [ o, b, o, b, b, o, b, o],
                     [ o, b, o, o, o, o, b, o],
                     [ o, o, o, b, b, o, o, o] ])
}
EXIT_SCREEN = {
"Exit": np.array([[r, w, k, k, k, k, w, k],
                  [w, r, k, r, r, k, k, w],
                  [k, w, r, k, k, r, w, k],
                  [k, r, k, r, k, k, r, k],
                  [k, r, k, k, r, k, r, k],
                  [k, k, r, k, k, r, k, k],
                  [k, k, k, r, r, k, r, k],
                  [k, k, k, k, k, k, k, r]
                  ])
}
