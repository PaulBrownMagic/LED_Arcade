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
        # Other stuff!
        self.translate = {"KEY_DOWN": DOWN,
                          "KEY_UP": UP,
                          "KEY_LEFT": LEFT,
                          "KEY_RIGHT": RIGHT}

    def _read_events(self):
        # self.stdscr.clear()  # Clear the screen
        while True:
            self.q.put(self.stdscr.getkey())  # Read the keys and put in the queue

    def get_events(self):
        events = []
        while not self.q.empty():  # Process the queue into events
            try:
                events.append(self.translate[self.q.get()])
            except KeyError:
                events.append(BUTTON)
        return events

    def cleanup(self):
        self.p.terminate()  # Join the running process: Uses SIGTERM
        curses.nocbreak()  # Require Return in the Terminal
        self.stdscr.keypad(False)  # Return to normal key representation
        curses.echo()  # Print out in the terminal
        curses.endwin()  # Restore terminal to normal
        print("Keyboard cleanup")  # Should print out fine
