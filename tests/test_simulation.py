import pytest

from exceptions import (
    AsteroidBoundariesNotSet,
    NoActiveRobots,
    AsteroidBoundariesAlreadySet,
    RobotOutsideBoundaries,
)


def test_calling_active_robot_with_no_robots_attached(test_simulation):
    with pytest.raises(NoActiveRobots):
        test_simulation.active_robot


def test_is_boundaries_set_method_with_no_boundaries(test_simulation):
    assert not test_simulation.is_boundaries_set()


def test_is_boundaries_set_method_with_boundaries_set(test_simulation):
    test_simulation.set_boundaries({"type": "asteroid", "size": {"x": 5, "y": 5}})
    assert test_simulation.is_boundaries_set()


def test_spawning_a_robot_with_no_boundaries_defined(test_simulation):
    with pytest.raises(AsteroidBoundariesNotSet):
        test_simulation.spawn_robot(
            {"type": "new-robot", "position": {"x": 3, "y": 3}, "bearing": "east"}
        )


def test_spawning_a_robot_with_boundaries_defined(test_simulation):
    test_simulation.boundaries = (2, 3)
    assert len(test_simulation.all_robots) == 0

    test_simulation.spawn_robot(
        {"type": "new-robot", "position": {"x": 1, "y": 2}, "bearing": "north"}
    )
    assert len(test_simulation.all_robots) == 1


def test_setting_boundaries(test_simulation):
    assert test_simulation.boundaries is None
    test_simulation.set_boundaries({"type": "asteroid", "size": {"x": 5, "y": 5}})

    assert test_simulation.boundaries == (5, 5)


def test_overwritting_boundaries(test_simulation):
    with pytest.raises(AsteroidBoundariesAlreadySet):
        test_simulation.boundaries = (5, 5)

        test_simulation.set_boundaries({"type": "asteroid", "size": {"x": 2, "y": 2}})


def test_executing_robot_command_with_no_boundaries_set(test_simulation):
    with pytest.raises(AsteroidBoundariesNotSet):
        test_simulation.execute_robot_command({"type": "move", "movement": "turn-left"})


def test_executing_robot_command_with_no_robots(test_simulation):
    test_simulation.boundaries = (2, 3)
    with pytest.raises(NoActiveRobots):
        test_simulation.execute_robot_command({"type": "move", "movement": "turn-left"})


def test_spawning_robot_outside_of_bounds(test_simulation):
    test_simulation.boundaries = (2, 3)
    with pytest.raises(RobotOutsideBoundaries):
        test_simulation.spawn_robot(
            {"type": "new-robot", "position": {"x": 3, "y": 3}, "bearing": "east"}
        )


def test_robot_moves_outside_of_bounds(test_simulation):
    test_simulation.boundaries = (2, 3)
    test_simulation.spawn_robot(
        {"type": "new-robot", "position": {"x": 2, "y": 3}, "bearing": "north"}
    )
    with pytest.raises(RobotOutsideBoundaries):
        test_simulation.execute_robot_command(
            {"type": "move", "movement": "move-forward"}
        )
