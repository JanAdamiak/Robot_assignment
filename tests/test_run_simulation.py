from main import run_simulation


def test_run_simulation(test_simulation, initial_commands_data):
    assert test_simulation.boundaries is None
    assert not test_simulation.all_robots

    new_simulation_output = run_simulation(test_simulation, initial_commands_data)
    assert new_simulation_output.boundaries == (5, 5)
    assert new_simulation_output.all_robots
