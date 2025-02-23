

from Simulation import Simulation, Network, Task, RuntimeControl, randomNetworkGenerator, randomTaskGenerator, simulationLength
import matplotlib.pyplot as plt

import numpy as np
import datetime
import matplotlib.pyplot as plt

# Define a function to count task distribution across devices and track energy consumption
def task_distribution_summary(runtimeControl, network):
    # Create a dictionary to track the number of tasks and energy consumption assigned to each device type
    distribution = {
        "cloud": {"tasks": 0, "energy": 0},
        "edge": {"tasks": 0, "energy": 0},
        "volunteer": {"tasks": 0, "energy": 0},
        "localDevice": {"tasks": 0, "energy": 0}
    }

    # Loop through each assigned task and count the assignments, also sum energy consumption
    for taskI in runtimeControl.assignedTasks:
        assigned_unit = taskI.assignedUnit
        unit_type = network.units[assigned_unit].getType()
        if unit_type in distribution:
            distribution[unit_type]["tasks"] += 1
            distribution[unit_type]["energy"] += network.units[assigned_unit].totalEnergyConsumed

    # Print the summary of task assignments and energy consumption
    print("Task Distribution Summary:")
    print(f"Cloud: {distribution['cloud']['tasks']} tasks, Energy: {distribution['cloud']['energy']} Wh")
    print(f"Edge: {distribution['edge']['tasks']} tasks, Energy: {distribution['edge']['energy']} Wh")
    print(f"Volunteer: {distribution['volunteer']['tasks']} tasks, Energy: {distribution['volunteer']['energy']} Wh")
    print(f"Local Device: {distribution['localDevice']['tasks']} tasks, Energy: {distribution['localDevice']['energy']} Wh")

    return distribution

# Define the main function that runs the simulation and analyzes task distribution and energy
def run_task_distribution_test(num_clouds, num_edges, num_volunteers, num_tasks):
    """
    Run the simulation to test task distribution across cloud, edge, volunteers, and local device.
    """
    # Generate the network with clouds, edges, and volunteers
    network = randomNetworkGenerator(num_clouds, num_edges)
    network.generateRandomVolunteers(num_volunteers)

    # Generate random tasks
    tasks = randomTaskGenerator(num_tasks, simulationLength)

    # Create the simulation object
    simulation = Simulation(network, tasks, "minimizeLatency")

    # Run the simulation (you can choose a specific shutdown or no-shutdown mode)
    runtimeControl = simulation.run()
    simulation.plotGanttChart()  # You can replace with other modes like runWithRandomShutdowns

    # Analyze the task distribution and energy consumption
    distribution = task_distribution_summary(runtimeControl, network)

    return distribution

# Parameters for the test
num_clouds = 1        # Number of cloud units
num_edges = 3         # Number of edge units
num_volunteers = 0    # Number of volunteer units
num_tasks = 2000      # Total number of tasks

# Run the test
task_distribution = run_task_distribution_test(num_clouds, num_edges, num_volunteers, num_tasks)

# Extract energy data for plotting
cloud_energy = task_distribution['cloud']['energy']
edge_energy = task_distribution['edge']['energy']
volunteer_energy = task_distribution['volunteer']['energy']
local_device_energy = task_distribution['localDevice']['energy']

# Plot energy consumption across device types
device_types = ['Cloud', 'Edge', 'Volunteers', 'Local Device']
energy_values = [cloud_energy, edge_energy, volunteer_energy, local_device_energy]

plt.figure(figsize=(10, 6))
plt.bar(device_types, energy_values, color=['blue', 'green', 'orange', 'red'])
plt.title('Energy Consumption by Device Type')
plt.xlabel('Device Type')
plt.ylabel('Total Energy Consumption (Wh)')
plt.grid(True)
plt.show()

import numpy as np
import datetime
import matplotlib.pyplot as plt

# Define a function to count task distribution across devices and track energy consumption
def task_distribution_summary(runtimeControl, network, total_tasks):
    # Create a dictionary to track the number of tasks and energy consumption assigned to each device type
    distribution = {
        "cloud": {"tasks": 0, "energy": 0},
        "edge": {"tasks": 0, "energy": 0},
        "volunteer": {"tasks": 0, "energy": 0},
        "localDevice": {"tasks": 0, "energy": 0},
        "unassigned": 0  # Track unassigned tasks
    }

    # Loop through each assigned task and count the assignments, also sum energy consumption
    for taskI in runtimeControl.assignedTasks:
        assigned_unit = taskI.assignedUnit
        if assigned_unit is not None:
            unit_type = network.units[assigned_unit].getType()
            if unit_type in distribution:
                distribution[unit_type]["tasks"] += 1
                distribution[unit_type]["energy"] += network.units[assigned_unit].totalEnergyConsumed
        else:
            distribution["unassigned"] += 1  # Count unassigned tasks

    # Calculate the missing tasks
    total_assigned_tasks = sum(distribution[unit]["tasks"] for unit in distribution if unit != "unassigned")
    unassigned_tasks = total_tasks - total_assigned_tasks

    # Print the summary of task assignments, unassigned tasks, and energy consumption
    print("Task Distribution Summary:")
    print(f"Cloud: {distribution['cloud']['tasks']} tasks, Energy: {distribution['cloud']['energy']} Wh")
    print(f"Edge: {distribution['edge']['tasks']} tasks, Energy: {distribution['edge']['energy']} Wh")
    print(f"Volunteer: {distribution['volunteer']['tasks']} tasks, Energy: {distribution['volunteer']['energy']} Wh")
    print(f"Local Device: {distribution['localDevice']['tasks']} tasks, Energy: {distribution['localDevice']['energy']} Wh")
    print(f"Unassigned tasks: {unassigned_tasks}")

    return distribution

# Define the main function that runs the simulation and analyzes task distribution and energy
def run_task_distribution_test(num_clouds, num_edges, num_volunteers, num_tasks):
    """
    Run the simulation to test task distribution across cloud, edge, volunteers, and local device.
    """
    # Generate the network with clouds, edges, and volunteers
    network = randomNetworkGenerator(num_clouds, num_edges)
    network.generateRandomVolunteers(num_volunteers)

    # Generate random tasks
    tasks = randomTaskGenerator(num_tasks, simulationLength)

    # Create the simulation object
    simulation = Simulation(network, tasks, "minimizeLatency")

    # Run the simulation (you can choose a specific shutdown or no-shutdown mode)
    runtimeControl = simulation.run()
    simulation.plotGanttChart()  # You can replace with other modes like runWithRandomShutdowns

    # Analyze the task distribution and energy consumption
    distribution = task_distribution_summary(runtimeControl, network, num_tasks)

    return distribution

# Parameters for the test
num_clouds = 1        # Number of cloud units
num_edges = 3         # Number of edge units
num_volunteers = 0    # Number of volunteer units
num_tasks = 2000      # Total number of tasks

# Run the test
task_distribution = run_task_distribution_test(num_clouds, num_edges, num_volunteers, num_tasks)

# Extract energy data for plotting
cloud_energy = task_distribution['cloud']['energy']
edge_energy = task_distribution['edge']['energy']
volunteer_energy = task_distribution['volunteer']['energy']
local_device_energy = task_distribution['localDevice']['energy']

# Plot energy consumption across device types
device_types = ['Cloud', 'Edge', 'Volunteers', 'Local Device']
energy_values = [cloud_energy, edge_energy, volunteer_energy, local_device_energy]

plt.figure(figsize=(10, 6))
plt.bar(device_types, energy_values, color=['blue', 'green', 'orange', 'red'])
plt.title('Energy Consumption by Device Type')
plt.xlabel('Device Type')
plt.ylabel('Total Energy Consumption (Wh)')
plt.grid(True)
plt.show()

