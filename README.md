# VonEdgeSim: Volunteer Edge Computing Simulation

**VonEdgeSim** is a simulation framework designed to evaluate the integration of volunteer computing with edge environments, specifically for IoT applications. This framework leverages the underutilized computational resources from volunteer devices at the network's edge, providing a scalable and resource-efficient solution.

## Design Overview

**VonEdgeSim** is structured to realistically simulate the dynamics of a volunteer edge computing (VEC) environment, incorporating a mix of cloud servers, edge devices, and volunteer devices, each with distinct performance characteristics and connectivity profiles.

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

### Running the Simulation

Clone the repository and navigate to the project directory:

```bash
git clone [repository-url]
cd [project-directory]
