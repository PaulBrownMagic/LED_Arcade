import numpy as np
from writer import Writer
import time

def welcome(display):
    """Scroll a welcome phrase across the display on load"""
    writer = Writer()
    writer.make_phrase(" ...arcade... ")
    for frame in writer.generate_frames():
        grid = np.dstack([frame, frame, frame]) * 255
        display.update(grid)
        time.sleep(0.2)
