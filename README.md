# Raspberry Pi LED arcade

Building on previous projects, including the Snake game with the Unicorn Hat
from Pimoroni, this project aims to assemble a collection of games with a user
interface to navigate them.

The project will be display agnostic, so a parameter can be set to choose
whether to use the Unicorn Hat, Sense Hat, or another 8*8 RGB LED display.
It will also be input agnostic, so again with a parameter the input can be
changed between SenseHat's onboard joystick, a keyboard or other gaming pad.

Games to be included are tributes to classics old and new, including snake,
pac-man, flappy bird and more.

Currently the project is developing the user interface and menu system before
beginning on the games. If you'd like to get involved, check out the TODO list
for the next jobs that need doing. Some of these are pretty easy!

\<TODO\>:
- [ ] UPPERCASE letters and more punctuation in letters.py ALPHABET
- [ ] Pretty animations for inbetweens in animations.py
- [x] Design menu system, perhaps colour coded or icons. Words will be  annoying
- [ ] Make a score display animation, e.g.: "Score: 12" in animations.py
- [x] Implement a FPS (frames per second) system, better than time.sleep()!
- [x] Pick a harder to input exit method: moved to menu.

\<One day...\>:
- [ ] Move menu screen to game class?
- [ ] Animated menu screens
- [ ] Lots of games!
- [ ] High Score view (press up/down in menu?)
