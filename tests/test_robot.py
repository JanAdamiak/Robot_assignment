import pytest

from robot import Robot
from enums import Bearing


def test_robot_initialisation():
    test_robot = Robot(1, 2, "north")

    assert test_robot.x == 1
    assert test_robot.y == 2
    assert test_robot.bearing == Bearing.north


def test_invalid_bearing_robot_initialisation():
    with pytest.raises(KeyError):
        Robot(1, 2, "abc")


@pytest.mark.parametrize(
    "bearing, expected",
    [("north", "west"), ("east", "north"), ("south", "east"), ("west", "south")],
)
def test_turn_left(bearing, expected):
    test_robot = Robot(1, 2, bearing)
    assert test_robot.bearing.name == bearing

    test_robot.turn_left()

    assert test_robot.bearing.name == expected


@pytest.mark.parametrize(
    "bearing, expected",
    [("north", "east"), ("east", "south"), ("south", "west"), ("west", "north")],
)
def test_turn_right(bearing, expected):
    test_robot = Robot(1, 2, bearing)
    assert test_robot.bearing.name == bearing

    test_robot.turn_right()

    assert test_robot.bearing.name == expected


@pytest.mark.parametrize(
    "robot_x, robot_y, bearing, expected_x, expected_y",
    [
        (1, 1, "north", 1, 2),
        (1, 0, "south", 1, -1),
        (4, 4, "west", 3, 4),
        (5, 5, "east", 6, 5),
    ],
)
def test_move(robot_x, robot_y, bearing, expected_x, expected_y):
    test_robot = Robot(robot_x, robot_y, bearing)

    assert test_robot.x == robot_x
    assert test_robot.y == robot_y
    assert test_robot.bearing.name == bearing

    test_robot.move()

    assert test_robot.x == expected_x
    assert test_robot.y == expected_y
    assert test_robot.bearing.name == bearing


@pytest.mark.parametrize(
    "robot_x, robot_y, bearing",
    [
        (1, 1, "north"),
        (1, 0, "south"),
        (4, 4, "west"),
        (5, 5, "east"),
    ],
)
def test_location_property(robot_x, robot_y, bearing):
    test_robot = Robot(robot_x, robot_y, bearing)

    assert test_robot.location == {
        "type": "robot",
        "position": {"x": robot_x, "y": robot_y},
        "bearing": bearing,
    }
