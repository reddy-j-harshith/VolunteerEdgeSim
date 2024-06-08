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

### Future Work

#### Adding Mobility and Autonomous Unmanned Systems (AUS)

To extend the VolunteerEdgeSim with mobility features or to integrate Autonomous Unmanned Systems (AUS), follow these steps:

1. **Modify the `GeneralUnit` Class:**
   - **Location Handling:** Enhance the handling of the `location` attribute to support dynamic updates. Implement methods to update the location based on mobility patterns.
   - **AUS-Specific Methods:** Override methods like `computeExecutionTime()` to incorporate AUS-specific factors such as varying connectivity depending on altitude or movement.

2. **Update the `Network` Class:**
   - **Dynamic Topology:** Augment the `Network` class to handle changes in topology dynamically as nodes move. This includes recalculating connectivity or routes based on new node positions.
   - **Node Management:** Add methods to dynamically manage nodes, allowing for AUS to enter or leave the network dynamically.

3. **Enhance the `Task` Class:**
   - **Mobility-Aware Task Management:** Adapt task assignment logic to account for node mobility, potentially reassigning tasks if a node moves out of effective range.
   - **Task Redundancy:** Implement mechanisms to manage task redundancy, improving robustness against the unpredictability of mobile nodes.

4. **Expand the `Simulation` Class:**
   - **Simulate Mobility:** Integrate mobility simulation within the main simulation loop, updating node positions periodically.
   - **Adapt Metrics:** Revise performance metrics to consider the impacts of mobility, such as potential increases in latency or task failures due to movement.

5. **Develop Utility Functions:**
   - **Mobility Models:** Create or integrate mobility models that define node movement within the simulation space, whether random, path-based, or mimicking real-world behaviors.
   - **AUS Logic:** Implement logic specific to AUS operations, including energy consumption related to mobility, payload management, and interactions with infrastructure.



