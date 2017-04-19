import numpy as np

from displays.letters import ALPHABET


class Writer:
    """Produce scrolling text for the LED display, frame by frame"""

    def __init__(self):
        self.font = ALPHABET
        self.spacer = np.zeros([8, 1], dtype=int)
        self.phrase = None

    def make_phrase(self, phrase):
        """Convert a string into a long numpy array with spacing"""
        # phrase.lower() called because ALPHABET currently doesn't have capitals
        converted = [np.hstack([self.font[letter], self.spacer])
                     for letter in phrase.lower()]
        self.phrase = np.hstack(converted)

    def generate_frames(self):
        """Produce single 8*8 frames scrolling across phrase"""
        height, width = np.shape(self.phrase)
        for frame in range(width - 8):
            yield self.phrase[:, frame:frame + 8]

    def write(self, phrase):
        """Easily get frames for a phrase"""
        self.make_phrase(phrase)
        for frame in self.generate_frames():
            yield frame
