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

### Future Work: Incorporating Vehicle Nodes into VolunteerEdgeSim

#### 1. Enhance the `GeneralUnit` Class:
   - **Location Dynamics:** Extend the location handling in the `GeneralUnit` class to accommodate the dynamic nature of vehicle nodes. Implement methods that update the location in real-time based on vehicular movement patterns.
   - **Connectivity Variation:** Adapt the `computeExecutionTime()` method to factor in connectivity variations that occur due to changes in the vehicle's location or network conditions.

#### 2. Update the `Network` Class:
   - **Dynamic Topology Management:** Modify the `Network` class to dynamically adjust to changes in the network topology as vehicle nodes move. This could involve recalculating connections or updating routing information to reflect the current positions of the vehicles.
   - **Vehicle Node Management:** Develop methods to dynamically add or remove vehicle nodes from the network, simulating real-world scenarios where vehicles may enter or exit certain network areas.

#### 3. Modify the `Task` Class:
   - **Mobility-Aware Task Assignment:** Revise the task assignment logic to consider the mobility of vehicle nodes. This may include strategies to reassign tasks if a vehicle moves out of the effective communication range.
   - **Task Redundancy for Vehicles:** Implement redundancy mechanisms to ensure task reliability, compensating for the unpredictable nature of vehicle nodes.

#### 4. Expand the `Simulation` Class:
   - **Simulate Vehicle Mobility:** Integrate a sub-module within the simulation loop that periodically updates the positions of vehicle nodes based on predefined or stochastic mobility patterns.
   - **Adjust Metrics for Mobility:** Update the performance metrics to account for the additional challenges introduced by vehicle mobility, such as increased latency and potential task failures.

#### 5. Develop Utility Functions:
   - **Mobility Models for Vehicles:** Implement or integrate existing mobility models that realistically represent the movements of vehicles within the simulation environment.
   - **Specific Logic for Vehicle Operations:** Develop functionalities that are specific to vehicles, such as managing the energy consumption that varies with speed and operational dynamics, handling vehicle-specific payloads, and interacting with traffic management infrastructure.

