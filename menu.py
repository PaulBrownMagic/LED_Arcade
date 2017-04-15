from games.constants import GAMES
from constants import NAV_SCREENS

class Menu:
    current = 0
    number_of_games = len(GAMES) - 1

    def handle_events(self, events):
        for event in events:
            if event == "left":
                Menu.current -= 1
            elif event == "right":
                Menu.current += 1
            elif event == "middle":
                self.selected = GAMES[Menu.current]
        # Boundary check
        Menu.current = 0 if Menu.current > Menu.number_of_games else Menu.current
        Menu.current = Menu.number_of_games if Menu.current < 0 else Menu.current

    def run_logic(self):
        pass

    @staticmethod
    def display_update():
        return NAV_SCREENS[GAMES[Menu.current]]
