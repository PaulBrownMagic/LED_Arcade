# Raspberry Pi LED arcade

Building on previous projects, including the Snake game with the Unicorn Hat from Pimoroni, this project aims to assemble a collection of games with a user interface to navigate them.

The project will be display agnostic, so a parameter can be set to choose
whether to use the Unicorn Hat, Sense Hat, or another 8*8 RGB LED display. It will also be input agnostic, so again with a parameter the input can be changed between SenseHat's onboard joystick, a keyboard or other gaming pad.

Games tagged for inclusion are tributes to classics old and new, including snake, pac-man, flappy bird and more.

Currently the project is developing the user interface and menu system before beginning to amass games, displays and inputs. If you'd like to get involved, check out the TODO list for the next jobs that need doing. Some of these are pretty easy, some are pretty fun!

## Lists of jobs
\<TODO\>:
- [ ] UPPERCASE letters and more punctuation in letters.py ALPHABET
- [ ] Pretty animations for in-betweens in animations.py
- [ ] Make a score display animation, e.g.: "Score: 12" in animations.py
- [ ] Template game with explanation to help other developers.
- [ ] Fix displays.\_\_init\_\_.Writer numpy >= 1.12.1 dependency to work with 1.8.1 on Raspberry Pi
- [ ] Single constants for config variables and game names (tidy up!)
- [ ] Implement Logging
- [ ] Set of unit tests for inputs, displays
- [ ] Known bugs: Pacman pass-through ghosts. Purple rain: 2 in one pixel (-2 lives)

\<LONG-TERM TODO\>:
- [ ] Move menu screen to game class?
- [ ] Animated menu screens
- [ ] Lots of games!
- [ ] High Score view (press up/down in menu?)
- [ ] High Score with 3 letter names input and stored: classic arcade style
- [ ] Add Wii-Mote input
- [ ] GamePad input, may require config program.

\<DONE in this release\>:
- Design menu system, perhaps colour coded or icons. Words will be  annoying
- Implement a FPS (frames per second) system, better than time.sleep()!
- Pick a harder to input exit method: moved to menu.
- Constants to describe input values, i.e. inputs.LEFT = "left"
- Config file to read in input and diplay choice.
- Command to write config file.
- Keyboard input

## Rules of engagement
1. Minimal dependencies: make this super easy to install and to learn from
2. Program for Python 3.x where x is the standard version available in Pixel on the Raspberry Pi, same for numpy etc.
3. Must run "headless": all communication to the user is through the LED display: be imaginative, clear and simple.
