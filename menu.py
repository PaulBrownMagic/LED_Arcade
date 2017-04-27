from constants import EXIT_SCREEN, NAV_SCREENS
from inputs import BUTTON, LEFT, RIGHT


class Menu:
    """Navigation/ Menu system for choosing a game"""
    fps = 0.1

    def __init__(self):
        self.current = 0
        self.screens = NAV_SCREENS
        self.screens.update(EXIT_SCREEN)  # Can remove quit option
        self.screen_names = list(self.screens.keys())
        self.number_of_screens = len(self.screens) - 1
        self.selected = None

    def process_events(self, events):
        for event in events:
            if event == LEFT:
                self.current -= 1
            elif event == RIGHT:
                self.current += 1
            elif event == BUTTON:
                self.selected = self.screen_names[self.current]
        # Boundary check
        self.current = 0 if self.current > self.number_of_screens else self.current
        self.current = self.number_of_screens if self.current < 0 else self.current

    def run_logic(self):
        pass

    def update_display(self):
        return self.screens[self.screen_names[self.current]]
