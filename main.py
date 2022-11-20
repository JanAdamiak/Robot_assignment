# Python imports
from typing import Dict, Any, List
import os
import json

# custom imports
from simulation import Simulation


def parse_txt_file(location: str) -> Dict[str, Any]:
    """Parse a text file in passed location, read it's contents and then return a list of dict's."""
    output = []

    with open(location, "r") as read_file:
        for line in read_file:
            output.append(json.loads(line.strip()))

    return output


def run_simulation(
    simulation: Simulation, commands: List[Dict[str, Any]]
) -> Simulation:
    """Pass a set of commands to the passed simulation."""
    for command in commands:
        func_to_execute = simulation.command_dispatcher[command["type"]]
        func_to_execute(command)

    simulation.get_output()

    return simulation


# get location of the command txt file
file_dir = os.path.abspath(os.curdir) + "/sample_file.txt"

# parse commands from txt file
parsed_commands = parse_txt_file(file_dir)

# Initiate a Simulation, pass the commands and ask all robots to emit their locations
my_simulation = Simulation()
my_simulation = run_simulation(my_simulation, parsed_commands)
