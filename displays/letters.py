import numpy as np

""" Dictionary of letters and punctuation for scrolling text, max height: 8 """

ALPHABET = {
    'a':
    np.array(
        [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [1, 1, 1, 1],
            [0, 0, 0, 1],
            [1, 1, 1, 1],
            [1, 0, 0, 1],
            [1, 1, 1, 1],
        ],
        dtype=int),
    'b':
    np.array(
        [
            [1, 0, 0, 0],
            [1, 0, 0, 0],
            [1, 0, 0, 0],
            [1, 1, 1, 1],
            [1, 0, 0, 1],
            [1, 0, 0, 1],
            [1, 0, 0, 1],
            [1, 1, 1, 1],
        ],
        dtype=int),
    'c':
    np.array(
        [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [1, 1, 1, 1],
            [1, 0, 0, 0],
            [1, 0, 0, 0],
            [1, 0, 0, 0],
            [1, 1, 1, 1],
        ],
        dtype=int),
    'd':
    np.array(
        [
            [0, 0, 0, 1],
            [0, 0, 0, 1],
            [0, 0, 0, 1],
            [1, 1, 1, 1],
            [1, 0, 0, 1],
            [1, 0, 0, 1],
            [1, 0, 0, 1],
            [1, 1, 1, 1],
        ],
        dtype=int),
    'e':
    np.array(
        [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [1, 1, 1, 1],
            [1, 0, 0, 1],
            [1, 1, 1, 1],
            [1, 0, 0, 0],
            [1, 1, 1, 1],
        ],
        dtype=int),
    'f':
    np.array(
        [
            [0, 1, 1, 1],
            [0, 1, 0, 0],
            [0, 1, 0, 0],
            [1, 1, 1, 1],
            [0, 1, 0, 0],
            [0, 1, 0, 0],
            [0, 1, 0, 0],
            [1, 1, 0, 0],
        ],
        dtype=int),
    'g':
    np.array(
        [
            [0, 0, 0, 0],
            [1, 1, 1, 1],
            [1, 0, 0, 1],
            [1, 0, 0, 1],
            [1, 1, 1, 1],
            [0, 0, 0, 1],
            [0, 0, 0, 1],
            [1, 1, 1, 1],
        ],
        dtype=int),
    'h':
    np.array(
        [
            [1, 0, 0, 0],
            [1, 0, 0, 0],
            [1, 0, 0, 0],
            [1, 1, 1, 1],
            [1, 0, 0, 1],
            [1, 0, 0, 1],
            [1, 0, 0, 1],
            [1, 0, 0, 1],
        ],
        dtype=int),
    'i':
    np.array(
        [
            [0],
            [1],
            [0],
            [1],
            [1],
            [1],
            [1],
            [1],
        ],
        dtype=int),
    'j':
    np.array(
        [
            [0, 0, 0],
            [0, 0, 1],
            [0, 0, 0],
            [0, 0, 1],
            [0, 0, 1],
            [0, 0, 1],
            [0, 0, 1],
            [1, 1, 1],
        ],
        dtype=int),
    'k':
    np.array(
        [
            [1, 0, 0, 0],
            [1, 0, 0, 0],
            [1, 0, 0, 1],
            [1, 0, 1, 0],
            [1, 1, 0, 0],
            [1, 1, 0, 0],
            [1, 0, 1, 0],
            [1, 0, 0, 1],
        ],
        dtype=int),
    'l':
    np.array([
        [1],
        [1],
        [1],
        [1],
        [1],
        [1],
        [1],
        [1],
    ], dtype=int),
    'm':
    np.array(
        [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1],
        ],
        dtype=int),
    'n':
    np.array(
        [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [1, 1, 1, 1],
            [1, 0, 0, 1],
            [1, 0, 0, 1],
            [1, 0, 0, 1],
            [1, 0, 0, 1],
        ],
        dtype=int),
    'o':
    np.array(
        [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [1, 1, 1, 1],
            [1, 0, 0, 1],
            [1, 0, 0, 1],
            [1, 0, 0, 1],
            [1, 1, 1, 1],
        ],
        dtype=int),
    'p':
    np.array(
        [
            [0, 0, 0, 0],
            [1, 1, 1, 1],
            [1, 0, 0, 1],
            [1, 0, 0, 1],
            [1, 1, 1, 1],
            [1, 0, 0, 0],
            [1, 0, 0, 0],
            [1, 0, 0, 0],
        ],
        dtype=int),
    'q':
    np.array(
        [
            [0, 0, 0, 0],
            [1, 1, 1, 1],
            [1, 0, 0, 1],
            [1, 0, 0, 1],
            [1, 1, 1, 1],
            [0, 0, 0, 1],
            [0, 0, 0, 1],
            [0, 0, 0, 1],
        ],
        dtype=int),
    'r':
    np.array(
        [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [1, 1, 1, 1],
            [1, 0, 0, 0],
            [1, 0, 0, 0],
            [1, 0, 0, 0],
            [1, 0, 0, 0],
        ],
        dtype=int),
    's':
    np.array(
        [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [1, 1, 1, 1],
            [1, 0, 0, 0],
            [1, 1, 1, 1],
            [0, 0, 0, 1],
            [1, 1, 1, 1],
        ],
        dtype=int),
    't':
    np.array(
        [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [1, 0, 0, 0],
            [1, 1, 1, 0],
            [1, 0, 0, 0],
            [1, 0, 0, 0],
            [1, 1, 1, 1],
        ],
        dtype=int),
    'u':
    np.array(
        [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [1, 0, 0, 1],
            [1, 0, 0, 1],
            [1, 0, 0, 1],
            [1, 0, 0, 1],
            [1, 1, 1, 1],
        ],
        dtype=int),
    'v':
    np.array(
        [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [1, 0, 0, 1],
            [1, 0, 0, 1],
            [1, 0, 0, 1],
            [1, 0, 0, 1],
            [0, 1, 1, 0],
        ],
        dtype=int),
    'w':
    np.array(
        [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1],
            [1, 1, 1, 1, 1],
        ],
        dtype=int),
    'x':
    np.array(
        [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [1, 0, 0, 1],
            [1, 0, 0, 1],
            [0, 1, 1, 0],
            [1, 0, 0, 1],
            [1, 0, 0, 1],
        ],
        dtype=int),
    'y':
    np.array(
        [
            [0, 0, 0, 0],
            [1, 0, 0, 1],
            [1, 0, 0, 1],
            [1, 0, 0, 1],
            [1, 1, 1, 1],
            [0, 0, 0, 1],
            [0, 0, 0, 1],
            [1, 1, 1, 1],
        ],
        dtype=int),
    'z':
    np.array(
        [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [1, 1, 1, 1],
            [0, 0, 0, 1],
            [1, 1, 1, 1],
            [1, 0, 0, 0],
            [1, 1, 1, 1],
        ],
        dtype=int),
    ' ':
    np.array(
        [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ],
        dtype=int),
    '.':
    np.array(
        [
            [0, 0],
            [0, 0],
            [0, 0],
            [0, 0],
            [0, 0],
            [0, 0],
            [1, 1],
            [1, 1],
        ],
        dtype=int),
}
