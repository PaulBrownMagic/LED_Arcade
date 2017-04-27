import curses
from multiprocessing import Process, Queue

from inputs import BUTTON, DOWN, LEFT, RIGHT, UP


class KeyboardInput:
    """Uses Curses module to read input keys directly"""

    def __init__(self):
        # Curses
        self.stdscr = curses.initscr()  # Initialise curses
        curses.noecho()  # Don't print to screens
        curses.cbreak()  # Don't require Return key between inputs
        self.stdscr.keypad(True)  # Give non-typing keys a nice name
        # Multiprocessing
        self.q = Queue()  # Use a queue to manage events between processes
        self.p = Process(target=self._read_events)  # Run event collection in own process
        self.p.start()

    def _read_events(self):
        # self.stdscr.clear()  # Clear the screen
        while True:
            self.q.put(self.stdscr.getkey())  # Read the keys and put in the queue

    def get_events(self):
        events = []
        while not self.q.empty():  # Prcess the queue
            k = self.q.get()
            if "DOWN" in k:
                events.append(DOWN)
            elif "UP" in k:
                events.append(UP)
            elif "LEFT" in k:
                events.append(LEFT)
            elif "RIGHT" in k:
                events.append(RIGHT)
            else:
                events.append(BUTTON)
        return events

    def cleanup(self):
        self.p.terminate()  # Join the running process: Uses SIGTERM
        curses.nocbreak()  # Require Return in the Terminal
        self.stdscr.keypad(False)  # Return to normal key representation
        curses.echo()  # Print out in the terminal
        curses.endwin()  # Restore terminal to normal
        print("Keyboard cleanup")  # Should print out fine
