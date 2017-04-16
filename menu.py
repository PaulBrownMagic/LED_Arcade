from constants import NAV_SCREENS, EXIT_SCREEN

class Menu:
    fps = 0.1

    def __init__(self):
        self.current = 0
        self.screens = NAV_SCREENS
        self.screens.update(EXIT_SCREEN) # Can remove quit option
        self.screen_names = list(self.screens.keys())
        self.number_of_screens = len(self.screens) - 1
        self.selected = None

    def handle_events(self, events):
        for event in events:
            if event == "left":
                self.current -= 1
            elif event == "right":
                self.current += 1
            elif event == "middle":
                self.selected = self.screen_names[self.current]
        # Boundary check
        self.current = 0 if self.current > self.number_of_screens else self.current
        self.current = self.number_of_screens if self.current < 0 else self.current

    def run_logic(self):
        pass

    @staticmethod
    def update_display():
        return self.screens[self.screen_names[self.current]]
