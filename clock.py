import time


class Clock:
    """Sleeps until at least time for next frame"""

    def reset_clock(self, fps):
        self.fps = fps
        self.start_time = time.perf_counter()

    def tick(self):
        """Pause for fps"""
        time.sleep(max(0, self.fps - (time.perf_counter() - self.start_time)))
        self.start_time = time.perf_counter()
