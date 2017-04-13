#!/usr/bin/python3
import animations
import displays
import inputs
import numpy as np
import time


class Arcade:
    """Entry point to system. Manage states and main loop

    This class will contain a list of possible states, such as Loading,
    Menu, Snake, Pac-Man, GameOver, HighScores. It will handle switching between
    these states and pass that state any input received. Each state will handle
    its own run_logic, which will return a grid for update_display to show.
    """

    def __init__(self):
        self.grid = np.zeros([8,8,3], dtype=int)
        self.display = displays.SenseHatDisplay()
        self.state = "Welcome"
        self.controller = inputs.SenseHatInput()
        self.events = []
        animations.welcome(self.display)

    def get_input(self):
        """Get input from controller, pass to state"""
        self.events = self.controller.get_events()
        for event in self.events:
            if event == "middle":
                self.state = "Exit"

    def run_logic(self):
        """Call state's run_logic and handle state change"""
        pass

    def update_display(self):
        """show the grid on self.display"""
        self.display.update(self.grid)

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
