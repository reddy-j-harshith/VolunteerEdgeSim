# VonEdgeSim: Volunteer Edge Computing Simulation

**VonEdgeSim** is a simulation framework designed to evaluate the integration of volunteer computing with edge environments, specifically for IoT applications. This framework leverages the underutilized computational resources from volunteer devices at the network's edge, providing a scalable and resource-efficient solution.

## Design Overview

**VonEdgeSim** is structured to realistically simulate the dynamics of a volunteer edge computing (VEC) environment, incorporating a mix of cloud servers, edge devices, and volunteer devices, each with distinct performance characteristics and connectivity profiles.

![sim_arch2 (1)](https://github.com/SimuEnv/VolunteerEdgeSim/assets/115349418/69164dcc-f368-48cd-8c54-ec91a0873b73)



### Key Components

#### General Unit Class

- **Superclass** for all devices including clouds, edges, volunteers, and the local device.
- Handles common attributes such as name, location, capacity, and costRate.
- Manages task computations and assignments considering transmission power and energy consumption.

#### Specific Device Classes

- **Cloud and Edge**: Inherits from GeneralUnit, potentially extended with cloud or edge-specific behaviors.
- **Volunteer**: Extends GeneralUnit with trust and availability management. Handles dynamic behaviors like shutdowns and trust restoration.
- **LocalDevice**: Represents the user's device initiating tasks.

#### Task Class

- Manages computational tasks with attributes like ID, type, priority, and resource requirements.
- Handles the task lifecycle including assignments and completions.

#### Network Class

- Manages a collection of device instances and facilitates dynamic additions of volunteers.

#### Simulation Class

- Core of the simulation, tying together the network and tasks.
- Distributes tasks based on specified optimization goals and handles dynamic network changes.

- ![digram](https://github.com/SimuEnv/VolunteerEdgeSim/assets/115349418/0c1a2182-b854-48e4-9980-5d3afd5f2cc9)


### Commands and Functional Flow

1. **Task Generation**: Utilizes `randomTaskGenerator` to create tasks with specific or random attributes.
2. **Network Setup**: Instantiates a network with clouds, edges, and volunteers.
3. **Simulation Execution**: Runs the simulation with dynamic volunteer behaviors and task assignments.
4. **Performance Metrics**: Tracks metrics such as task delay, execution time, and unassigned tasks.
5. **Visualization and Outputs**: Includes functionalities for visualizing the simulation results using Gantt charts or other methods.

## Getting Started

To run the simulation, ensure you have the required libraries installed, and configure the network and task parameters as needed.

### Prerequisites

- Python 3.x
- Numpy
- Pandas
- Matplotlib
- Plotly (for advanced visualizations)

## Running the Simulation

Clone the repository and navigate to the project directory:

```bash
git clone https://github.com/SimuEnv/VolunteerEdgeSim.git
cd VolunteerEdgeSim
```


## Using Jupyter Notebook for Initial Testing and Customization

For a flexible testing environment and to see all functions, including memory usage performance in action, you can use the Jupyter notebook:

```bash
jupyter notebook VolunteerEdgeSim.ipynb
```



Run all the cells in the notebook to check the simulation's behavior and output. You can adjust functions or add new features such as mobility functions or additional resources like Autonomous Unmanned Systems directly within the notebook.

Using the Main Script
After customizing the simulation to your liking in the notebook, you can execute the main simulation script to run the simulation from the command line:

## Future Work

### Adding Mobility

To integrate mobility into the simulation, researchers can start by modifying the `GeneralUnit` class to include mobility attributes that reflect the dynamic location changes of mobile units. This could involve adding methods that update the unit's location at each simulation tick based on a mobility model (e.g., Random Waypoint, Gauss-Markov).

**Steps to Implement Mobility:**
1. **Extend GeneralUnit Class:** Add attributes to store current location and speed.
2. **Update Location:** Implement a method in the `GeneralUnit` class that updates the location based on the chosen mobility model.
3. **Simulation Integration:** Ensure that the task assignment logic in `Simulation` class takes into account the changing locations of units when assigning tasks.

### Integrating UAS Drones

Incorporating Unmanned Aerial Systems (UAS) involves extending the simulation to handle the specific characteristics of drones, such as flight dynamics, energy consumption, and payload capacity. Drones can be modeled as a new class derived from `GeneralUnit`, with additional methods to manage their aerial capabilities.

**Steps to Integrate UAS Drones:**
1. **Create Drone Class:** Develop a `Drone` class deriving from `GeneralUnit`, including specific attributes like altitude, battery life, and payload.
2. **Flight Dynamics:** Implement methods to manage takeoff, landing, and in-flight behavior, considering energy consumption and battery recharging strategies.
3. **Task Assignment:** Adjust the task assignment algorithms in the `Simulation` class to factor in drone availability, flight range, and operational constraints.

### General Guidelines

- **Documentation:** Clearly document any changes or additions to the codebase, including how to use the new features.
- **Modularity:** Aim for modular changes that can be toggled on or off, allowing simulations with or without new features like mobility or drones.
- **Testing:** Thoroughly test new features to ensure they integrate seamlessly with the existing simulation framework without introducing bugs.

Researchers are encouraged to use these guidelines as a starting point for further development and to adapt the steps as necessary based on specific requirements of their simulation scenarios.


```bash
python main.py
```

