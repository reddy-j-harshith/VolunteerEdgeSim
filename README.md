VonEdgeSim: Simulation Design and Command Overview

The simulation code provided is designed to evaluate distributed network systems involving clouds, edges, volunteers, and a local device. The goal is to effectively distribute a set of tasks among these devices to optimize performance metrics such as execution time and energy consumption.

Design Highlights:
GeneralUnit Class:

Acts as the superclass for all device types (cloud, edge, volunteer, localDevice).
Manages attributes common to all units such as name, location, capacity, and costRate.
Includes methods for computing execution times and managing task assignments, considering factors like transmission power and energy consumption.
Specific Device Classes:

Cloud and Edge: Inherits from GeneralUnit. Custom methods or properties can be added to specify behaviors particular to cloud or edge environments.
Volunteer: Extends GeneralUnit with additional attributes like trust and availability. Includes methods to manage dynamic behaviors like shutdowns and trust restoration.
LocalDevice: A specialized form of GeneralUnit representing the user's device, initiating tasks.
Task Class:

Represents computational tasks with attributes like ID, type, priority, timing, and resource requirements.
Includes methods to manage task lifecycle such as assignment, reassignment, and completion tracking.
Network Class:

Manages a collection of all device instances (clouds, edges, volunteers, local).
Facilitates adding new volunteer units dynamically to the simulation.
Simulation Class:

Core class that ties together the network and tasks to run the simulation.
Manages the distribution of tasks based on the specified optimization goal (e.g., minimize latency).
Handles dynamic changes within the network, such as random shutdowns or reactivations of volunteer units.
Commands and Functional Flow:
Task Generation:

Tasks are generated with predefined or random attributes influencing their complexity and resource demands.
randomTaskGenerator function is used to create a set list of tasks based on the simulation requirements.
Network Setup:

A network is instantiated with a specified number of cloud and edge units.
Volunteers can be added dynamically to the network to study their impact on the system’s performance.
Simulation Execution:

The simulation is initiated with a set of tasks and runs according to the defined optimization goals.
Task assignment is managed by evaluating each device’s capability to handle the task within the required parameters.
Dynamic behavior like volunteer shutdown and turn-on is simulated to assess the robustness of the network.
Performance Metrics:

The system tracks and logs various metrics like task delay, execution time, and unassigned tasks.
Provides insights into how different configurations and volunteer behaviors impact the overall system performance.
