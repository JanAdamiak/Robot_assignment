class AsteroidBoundariesNotSet(Exception):
    """
    Exception raised for errors when trying to do robot specific actions
    and the asteroid boundaries haven't been setup.
    """

    def __str__(self) -> str:
        return "Asteroid with x and y boundaries has not been set"


class AsteroidBoundariesAlreadySet(Exception):
    """Exception raised for errors when trying to set up boundaries and they are already set."""

    def __str__(self) -> str:
        return "Asteroid with boundaries has already been set, can't overwrite the boundaries."


class NoActiveRobots(Exception):
    """Exception raised for errors when calling active robot and simulation has no robots attached."""

    def __str__(self) -> str:
        return "There are no active robots!"


class RobotOutsideBoundaries(Exception):
    """Exception raised for errors when active robot ends up outside of the permitted boundaries"""

    def __str__(self) -> str:
        return "Robot outside of the permitted boundaries!"
