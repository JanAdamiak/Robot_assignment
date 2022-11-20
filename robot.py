# Python imports
from typing import Dict, Any
from enums import Bearing


class Robot:
    def __init__(self, x: int, y: int, bearing: str) -> None:
        self.x = x
        self.y = y
        self.bearing = Bearing[bearing]

    @property
    def command_dispatcher(self) -> callable:
        return {
            "turn-left": self.turn_left,
            "turn-right": self.turn_right,
            "move-forward": self.move,
        }

    def _turn(self, direction: int) -> None:
        current_bearing = self.bearing.value
        new_bearing_value = (current_bearing + direction) % 4
        self.bearing = Bearing(new_bearing_value)

    def turn_right(self) -> None:
        """Turn the robot right, by changing it's bearing."""
        self._turn(1)

    def turn_left(self) -> None:
        """Turn the robot left, by changing it's bearing."""
        self._turn(-1)

    def move(self) -> None:
        """Move the robot 1 unit in the direction matching its bearing."""
        if self.bearing == Bearing.north:
            self.y = self.y + 1

        elif self.bearing == Bearing.east:
            self.x = self.x + 1

        elif self.bearing == Bearing.south:
            self.y = self.y - 1

        elif self.bearing == Bearing.west:
            self.x = self.x - 1

    @property
    def location(self) -> Dict[str, Any]:
        return {
            "type": "robot",
            "position": {"x": self.x, "y": self.y},
            "bearing": self.bearing.name,
        }
