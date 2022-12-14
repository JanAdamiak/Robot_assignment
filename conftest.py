import pytest

from simulation import Simulation


@pytest.fixture()
def initial_commands_data():
    return [
        {"type": "asteroid", "size": {"x": 5, "y": 5}},
        {"type": "new-robot", "position": {"x": 1, "y": 2}, "bearing": "north"},
        {"type": "move", "movement": "turn-left"},
        {"type": "move", "movement": "move-forward"},
        {"type": "move", "movement": "turn-left"},
        {"type": "move", "movement": "move-forward"},
        {"type": "move", "movement": "turn-left"},
        {"type": "move", "movement": "move-forward"},
        {"type": "move", "movement": "turn-left"},
        {"type": "move", "movement": "move-forward"},
        {"type": "move", "movement": "move-forward"},
        {"type": "new-robot", "position": {"x": 3, "y": 3}, "bearing": "east"},
        {"type": "move", "movement": "move-forward"},
        {"type": "move", "movement": "move-forward"},
        {"type": "move", "movement": "turn-right"},
        {"type": "move", "movement": "move-forward"},
        {"type": "move", "movement": "move-forward"},
        {"type": "move", "movement": "turn-right"},
        {"type": "move", "movement": "move-forward"},
        {"type": "move", "movement": "turn-right"},
        {"type": "move", "movement": "turn-right"},
        {"type": "move", "movement": "move-forward"},
    ]


@pytest.fixture()
def test_simulation():
    return Simulation()
