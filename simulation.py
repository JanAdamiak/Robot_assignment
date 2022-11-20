# Python imports
from typing import Dict, Any, List, Tuple

# Custom imports
from robot import Robot
from utils import validate_bounds
from exceptions import (
    AsteroidBoundariesNotSet,
    NoActiveRobots,
    AsteroidBoundariesAlreadySet,
    RobotOutsideBoundaries,
)


class Simulation:
    def __init__(self) -> None:
        self.boundaries: Tuple(int, int) = None
        self.all_robots: List[Robot] = []

    @property
    def active_robot(self) -> Robot:
        try:
            return self.all_robots[-1]
        except IndexError as exc:
            raise NoActiveRobots() from exc

    @property
    def command_dispatcher(self) -> callable:
        return {
            "asteroid": self.set_boundaries,
            "new-robot": self.spawn_robot,
            "move": self.execute_robot_command,
        }

    def is_boundaries_set(self) -> bool:
        """Check if boundaries set for the Simulation object."""
        if self.boundaries is None:
            return False
        return True

    def set_boundaries(self, command: Dict[str, Any]) -> None:
        """
        Set boundaries based on the command coordinates passed.
        If boundaries already set will raise an exception.
        """
        if self.is_boundaries_set():
            raise AsteroidBoundariesAlreadySet()

        self.boundaries = (command["size"]["x"], command["size"]["y"])

    def validate_robot_position(self) -> None:
        """Validate if the robot is within the bounds."""
        if not validate_bounds(
            0, self.boundaries[0], self.active_robot.x
        ) or not validate_bounds(0, self.boundaries[1], self.active_robot.y):
            raise RobotOutsideBoundaries()

    def spawn_robot(self, command: Dict[str, Any]) -> None:
        """
        Spawn robot with parameters based on the passed command.
        If boundaries not set will raise an exception.
        """
        if not self.is_boundaries_set():
            raise AsteroidBoundariesNotSet()

        new_robot = Robot(
            command["position"]["x"], command["position"]["y"], command["bearing"]
        )
        self.all_robots.append(new_robot)

        self.validate_robot_position()

    def execute_robot_command(self, command: Dict[str, Any]) -> None:
        """
        Try to move the active robot based on the command passed.
        If boundaries not set will raise an exception.
        """
        if not self.is_boundaries_set():
            raise AsteroidBoundariesNotSet()

        self.active_robot.command_dispatcher[command["movement"]]()

        self.validate_robot_position()

    def get_output(self) -> None:
        """
        Prints location based output for each robot in the simulation.
        Ordered by the order of robots spawning.
        """
        for robot in self.all_robots:
            print(robot.location)
