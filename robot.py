class Robot:
    """A simple 2D robot prototype."""

    def __init__(self, x=0, y=0, orientation='N'):
        self.x = x
        self.y = y
        self.orientation = orientation  # N, E, S, W

    def move_forward(self, steps=1):
        if self.orientation == 'N':
            self.y += steps
        elif self.orientation == 'E':
            self.x += steps
        elif self.orientation == 'S':
            self.y -= steps
        elif self.orientation == 'W':
            self.x -= steps
        else:
            raise ValueError(f'Unknown orientation {self.orientation}')

    def turn_left(self):
        orientation_order = 'NESW'
        idx = orientation_order.index(self.orientation)
        self.orientation = orientation_order[(idx - 1) % len(orientation_order)]

    def turn_right(self):
        orientation_order = 'NESW'
        idx = orientation_order.index(self.orientation)
        self.orientation = orientation_order[(idx + 1) % len(orientation_order)]

    def position(self):
        return self.x, self.y, self.orientation


if __name__ == '__main__':
    robot = Robot()
    print('Initial position:', robot.position())
    robot.move_forward()
    robot.turn_right()
    robot.move_forward(2)
    print('Final position:', robot.position())
