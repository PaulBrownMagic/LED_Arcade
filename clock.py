import time

class Clock:

    def reset_clock(self, fps):
        self.fps = fps
        self.start_time = time.perf_counter()

    def tick(self):
        time.sleep(max(self.fps - (time.perf_counter() - self.start_time, 0)))
        self.start_time = time.perf_counter()
