from games.constants import HORIZONTAL, VERTICAL


class Co_ordinates:
    """ 8*8 Co-ordinate values with self.x, self.y"""

    def __init__(self, position=[None, None]):
        self.set(position)

    def __setattr__(self, attribute, value):
        if attribute not in ["x", "y"]:  # Only allow pre-determined Co-ordinates
            raise ValueError("Invalid attribute for Co-ordinate (x, y)")
        if value is None:
            super().__setattr__(attribute, value)  # Allow None
        elif 0 <= int(value) <= 7:  # Restrict to display
            super().__setattr__(attribute, int(value))  # Else force int
        else:
            raise ValueError("Out of Range (0 to 7)")

    def __setitem__(self, key, value):
        if key == 0:
            self.x = value
        elif key == 1:
            self.y = value
        else:
            raise IndexError

    def __getitem__(self, key):
        return [self.x, self.y][key]  # c[0] = self.x

    def __len__(self):
        return len([self.x, self.y])

    def __iter__(self):
        yield "x", self.x
        yield "y", self.y

    def __eq__(self, other):
        # Could change to self.x == other[0] for versatility
        return self.x == other.x and self.y == other.y

    def set(self, position):
        self.x = position[0]
        self.y = position[1]


class Sprite:

    vertical_movements = {"up": (0, -1),
                          "down": (0, 1),
                          }
    horizontal_movements = {"left": (-1, 0),
                            "right": (1, 0)}
    horizontal = ["left", "right"]
    vertical = ["up", "down"]

    def __init__(self, movement_axis, no_double_back=False, solid_boundaries=True):
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
        self.position = Co_ordinates()
        self.solid_boundaries = solid_boundaries

    def event_response(self, direction):
        """Respond to event direction by updating self.change"""
        # If Sprite can't double back and movement invalid, return
        if self.no_double_back:
            if direction in self.horizontal and self.last_direction in self.horizontal:
                return
            elif direction in self.vertical and self.last_direction in self.vertical:
                return
            else:
                self.last_direction = direction
        # Otherwise, attempt to update self.change
        try:
            change = self.movement[direction]
        except KeyError:  # Invalid input, doesn't matter what, don't move!
            return
        # 1-axis movement
        if self.valid_axis == 1:
            self.change = sum(change)  # One value of change will be 0
        # 2-axis movement
        elif self.valid_axis == 2:
            self.change = change

    def _1_axis_move(self, axis, position=None):
        """Private method, move Sprite on a 1-D axis"""
        if not position:
            position = self.position
        new_position = position[axis] + self.change
        # Boundary check
        if self.solid_boundaries:
            # Stay within boudaries
            new_position = 7 if new_position > 7 else new_position
            new_position = 0 if new_position < 0 else new_position
        else:
            # Loop around display, i.e. from top to bottom or from left to right
            new_position = 0 if new_position > 7 else new_position
            new_position = 7 if new_position < 0 else new_position
        position[axis] = new_position
        return position

    def _2_axis_move(self, position=None):
        """Private method, move Sprite on 2 axis"""
        if not position:
            position = self.position
        new_x = position[0] + self.change[0]
        new_y = position[1] + self.change[1]
        # Boundary check
        if self.solid_boundaries:
            # Stay within boudaries
            new_x = 7 if new_x > 7 else new_x
            new_x = 0 if new_x < 0 else new_x
            new_y = 7 if new_y > 7 else new_y
            new_y = 0 if new_y < 0 else new_y
        else:
            # Loop around display, i.e. from top to bottom or from left to right
            new_x = 0 if new_x > 7 else new_x
            new_x = 7 if new_x < 0 else new_x
            new_y = 0 if new_y > 7 else new_y
            new_y = 7 if new_y < 0 else new_y
        return new_x, new_y

    def move(self, position=None):
        """Move the sprite, returns new_x, new_y, doesn't update self.position"""
        if self.valid_axis == 1 and "left" in self.movement.keys():
            return self._1_axis_move(axis=0, position=position)
        elif self.valid_axis == 1 and "up" in self.movement.keys():
            return self._1_axis_move(axis=1, position=position)
        elif self.valid_axis == 2:
            return self._2_axis_move(position)

    def update_position(self, position=None):
        """Move the Sprite, updates self.position to new value"""
        self.position.set(self.move(position))
