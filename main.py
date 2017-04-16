#!/usr/bin/python3
import animations
from displays.sensehat_display import SenseHatDisplay
from inputs.sensehat_input import SenseHatInput
from menu import Menu
import numpy as np
from games import purple_rain, snake
import time


class Arcade:
    """Entry point to system. Manage states and main loop

    This class will contain a list of possible states, such as Loading,
    Menu, Snake, Pac-Man, GameOver, HighScores. It will handle switching between
    these states and pass that state any input received. Each state will handle
    its own run_logic, which will return a grid for update_display to show.
    """

    def __init__(self):
        self.display = SenseHatDisplay()
        self.controller = SenseHatInput()
        self.menu = Menu()
        self.view = self.menu  # What part of the program currently shown/run
        self.game = None
        self.state = "Welcome"

        animations.welcome(self.display)

    # Generic functions for all views
    def get_input(self):
        """Get input from controller, pass to view"""
        events = self.controller.get_events()
        #for event in events:
        #    if event == "middle":
        #        self.state = "Exit"
        self.view.handle_events(events)

    def run_logic(self):
        """Call view's run_logic"""
        self.view.run_logic()

    def update_display(self):
        """Show the view on self.display"""
        if self.state == "Exit":
            self.display.clear()
        else:
            self.display.update(self.view.update_display())

    def frame(self):
        """Make a frame and display it"""
        self.get_input()
        self.run_logic()
        self.update_display()
        time.sleep(self.view.fps)

    # Specific loops for game and menu
    def game_loop(self):
        """Run the program until exit state is called"""
        while self.game and not self.game.game_over:
            self.frame()
        # Game Over, play animation
        animations.game_over(self.display)
        # Reset for menu and clear game
        self.game = None
        self.view = self.menu

    def menu_loop(self):
        """Run the program until exit state is called"""
        while not self.menu.selected:
            self.frame()
        print(self.menu.selected)
        # Select chosen game
        if self.menu.selected == "Snake":
            self.game = snake.Game()
        elif self.menu.selected == "Purple Rain":
            self.game = purple_rain.Game()
        # Load new game into view
        self.view = self.game

    # Show the menu, play a game. Rinse and repeat.
    def program_loop(self):
        while not self.state == "Exit":
            self.menu_loop()
            self.game_loop()


if __name__ == "__main__":
    arcade = Arcade()
    arcade.program_loop()
