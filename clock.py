import time

class Clock:

    def reset_clock(self, fps):
        self.fps = fps
        self.start_time = time.perf_counter()

    def tick(self):
        time.sleep(self.fps - (time.perf_counter() - self.start_time))
        self.start_time = time.perf_counter()