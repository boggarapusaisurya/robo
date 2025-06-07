from robot import Robot

def test_robot_moves():
    r = Robot()
    r.move_forward()
    assert r.position() == (0, 1, 'N')
    r.turn_right()
    r.move_forward(2)
    assert r.position() == (2, 1, 'E')
