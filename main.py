#!/usr/bin/python3
import animations
import displays
import inputs
import numpy as np
from games import snake
import time


class Arcade:
    """Entry point to system. Manage states and main loop

    This class will contain a list of possible states, such as Loading,
    Menu, Snake, Pac-Man, GameOver, HighScores. It will handle switching between
    these states and pass that state any input received. Each state will handle
    its own run_logic, which will return a grid for update_display to show.
    """

    def __init__(self):
        self.display = displays.SenseHatDisplay()
        self.controller = inputs.SenseHatInput()
        self.game = snake.Game()
        self.state = "Welcome"
        self.events = None

        animations.welcome(self.display)

    def get_input(self):
        """Get input from controller, pass to state"""
        self.events = self.controller.get_events()
        for event in self.events:
            if event == "middle":
                self.state = "Exit"
        self.game.handle_events(self.events)

    def run_logic(self):
        """Call state's run_logic and handle state change"""
        self.game.run_logic()

    def update_display(self):
        """show the grid on self.display"""
        if self.game.game_over:
            animations.game_over(self.display)
            self.game.game_over = False
            self.game.start = True
        if self.state == "Exit":
            self.display.clear()
        else:
            self.display.update(self.game.update_display())

    def game_loop(self):
        """Run the program until exit state is called"""
        while self.state != "Exit":
            self.get_input()
            self.run_logic()
            self.update_display()
            time.sleep(0.1)


if __name__ == "__main__":
    arcade = Arcade()
    arcade.game_loop()
