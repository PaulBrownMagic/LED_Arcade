#!/usr/bin/python3
import animations
from clock import Clock
from displays import load_display
from games import load_game
from inputs import load_controller
from menu import Menu


class Arcade:
    """Entry point to system. Manage states and main loop

    This class will contain a list of possible states, such as Loading,
    Menu, Snake, Pac-Man, GameOver, HighScores. It will handle switching between
    these states and pass that state any input received. Each state will handle
    its own run_logic, which will return a grid for update_display to show.
    """

    def __init__(self):
        self.display = load_display()
        self.controller = load_controller()
        self.menu = Menu()
        self.view = self.menu  # What part of the program currently shown/run
        self.game = None
        self.state = "Welcome"
        self.clock = Clock()
        animations.welcome(self.display)

    # Generic functions for all views
    def get_input(self):
        """Get input from controller, pass to view"""
        events = self.controller.get_events()
        self.view.process_events(events)

    def run_logic(self):
        """Call view's run_logic"""
        self.view.run_logic()

    def update_display(self):
        """Show the view on self.display"""
        self.display.update(self.view.update_display())

    def frame(self):
        """Make a frame and display it"""
        self.get_input()
        self.run_logic()
        self.update_display()
        self.clock.tick()

    # Specific loops for game and menu
    def game_loop(self):
        """Run the program until exit state is called"""
        self.clock.reset_clock(self.game.fps)
        while not self.game.game_over:
            self.frame()
        # Game Over, play animation
        animations.game_over(self.display)
        # Reset for menu, clear game and events
        self.game = None
        self.view = self.menu
        self.controller.get_events()

    def menu_loop(self):
        """Run the program until exit state is called"""
        self.clock.reset_clock(self.menu.fps)
        while not self.menu.selected:
            self.frame()
        # Select chosen game
        if self.menu.selected == "Exit":
            self.state = "Exit"
            return
        else:
            self.game = load_game(self.menu.selected)
        # Load new game into view
        self.menu.selected = None
        self.view = self.game

    # Show the menu, play a game. Rinse and repeat.
    def program_loop(self):
        # Ordered to allow for clean exiting from menu
        self.menu_loop()
        while not self.state == "Exit":
            self.game_loop()
            self.menu_loop()


if __name__ == "__main__":
    try:
        arcade = Arcade()
        arcade.program_loop()
    except Exception as e:
        print("\nERROR: {}\n\n".format(e.with_traceback(e)))
    finally:
        arcade.controller.cleanup()
        arcade.display.clear()
        print("Goodbye!")
