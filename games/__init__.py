from games.constants import HORIZONTAL, VERTICAL

class Sprite:

    vertical_movements = {"up": (0, -1),
                          "down": (0, 1),
                          }
    horizontal_movements = {"left": (-1, 0),
                            "right": (1, 0)}
    horizontal = ["left", "right"]
    vertical = ["up", "down"]

    def __init__(self, movement_axis, no_double_back=False):
        self.movement = dict()
        self.valid_axis = 0
        if HORIZONTAL in movement_axis:
            self.movement.update(self.horizontal_movements)
            self.valid_axis += 1
        if VERTICAL in movement_axis:
            self.movement.update(self.vertical_movements)
            self.valid_axis += 1
        self.no_double_back = no_double_back
        self.last_direction = None
        self.change = None

    def move(self, direction):
        if self.no_double_back:
            if direction in self.horizontal and self.last_direction in self.horizontal:
                return
            elif direction in self.vertical and self.last_direction in self.vertical:
                return
            else:
                self.last_direction = direction
        try:
            change = self.movement[direction]
        except KeyError:  # Invalid input, doesn't matter what, don't move!
            return
        # 2-axis movement
        if self.valid_axis == 2:
            self.change = change
        # 1-axis movement
        elif self.valid_axis == 1:
            self.change = sum(change)
