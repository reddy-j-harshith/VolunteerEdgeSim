import datetime
import numpy as np
from GeneralUnit import GeneralUnit
from Cloud import Cloud
from Edge import Edge
from Volunteer import Volunteer
from LocalDevice import LocalDevice
#from Task import Task, randomTaskGenerator
from Network import Network, randomNetworkGenerator
from RuntimeControl import RuntimeControl
from Simulation import Simulation

# Define urgency levels with different requirements
urgency_levels = {
    'low': {'priority': 1, 'min_deadline': 300, 'max_deadline': 900, 'delay_tolerance': 0.5},
    'medium': {'priority': 2, 'min_deadline': 180, 'max_deadline': 600, 'delay_tolerance': 0.3},
    'high': {'priority': 3, 'min_deadline': 60, 'max_deadline': 300, 'delay_tolerance': 0.1}
}

# Function to generate tasks with urgency levels
def healthcareTaskGenerator(num_tasks, urgency_level):
    tasks = []
    for i in range(num_tasks):
        # Task parameters vary based on urgency level
        params = urgency_levels[urgency_level]
        memory_size = np.random.uniform(1, 10)  # in MB
        CPU_cycles = np.random.uniform(100, 500) * memory_size
        arrival_time = datetime.datetime.now() + datetime.timedelta(seconds=np.random.uniform(0, 3600))
        # Reduce min and max deadlines to make tasks more challenging
        min_deadline = params['min_deadline'] / 2
        max_deadline = params['max_deadline'] / 2
        deadline_time = arrival_time + datetime.timedelta(seconds=np.random.uniform(min_deadline, max_deadline))

        task = Task(
            id=i,
            type='Healthcare',
            priority=params['priority'],
            arrivalTime=arrival_time,
            deadlineTime=deadline_time,
            delayTolerance=params['delay_tolerance'],
            CPUcycles=CPU_cycles,
            memorySize=memory_size,
            incentive=np.random.uniform(0.1, 1)
        )
        tasks.append(task)
    return tasks

# Initialize and run the simulation
def run_simulation(urgency_level, num_volunteers, num_tasks, use_trust=True):
    Nclouds = 1
    Nedges = 5
    Nvolunteers = num_volunteers
    Ntasks = num_tasks

    network = randomNetworkGenerator(Nclouds, Nedges)
    network.generateRandomVolunteers(Nvolunteers)

    tasks = healthcareTaskGenerator(Ntasks, urgency_level)

    if use_trust:
        simulation = Simulation(network, tasks, "minimizeLatency")
    else:
        simulation = SimulationNoTrust(network, tasks, "minimizeLatency")

    # Increase failure rates by decreasing shutDownFreq and increasing turnOnFreq
    shutDownFreq = 3  # Volunteers shut down more frequently
    turnOnFreq = 80   # Volunteers turn on less frequently

    runtimeControl = simulation.runWithRandomShutdowns(shutDownFreq, turnOnFreq)

    # Calculate KPIs
    total_delay = simulation.totalTasksDelay()
    not_assigned_tasks = runtimeControl.getNotAssignedTasks()
    completed_tasks = len([task for task in tasks if task.successFlag])
    failed_tasks = not_assigned_tasks
    average_latency = np.mean([task.getQueingTime().total_seconds() for task in tasks if task.successFlag])
    average_completion_time = np.mean([task.getExecutionTime().total_seconds() for task in tasks if task.successFlag])
    task_success_rate = completed_tasks / num_tasks * 100
    task_failure_rate = failed_tasks / num_tasks * 100
    max_queue_time = np.max([task.getQueingTime().total_seconds() for task in tasks if task.successFlag])
    min_queue_time = np.min([task.getQueingTime().total_seconds() for task in tasks if task.successFlag])
    stddev_completion_time = np.std([task.getExecutionTime().total_seconds() for task in tasks if task.successFlag])

    # Return results as a dictionary
    return {
        "Urgency Level": urgency_level,
        "Trust Enabled": use_trust,
        "Number of Volunteers": num_volunteers,
        "Number of Tasks": num_tasks,
        "Total tasks delay": total_delay,
        "Number of not assigned tasks": not_assigned_tasks,
        "Total tasks completed": completed_tasks,
        "Total tasks failed": failed_tasks,
        "Average latency": average_latency,
        "Average task completion time": average_completion_time,
        "Task success rate (%)": task_success_rate,
        "Task failure rate (%)": task_failure_rate,
        "Max queue time": max_queue_time,
        "Min queue time": min_queue_time,
        "Stddev completion time": stddev_completion_time
    }

# Lists to store results
results = []

# Run simulations for each urgency level with varying numbers of volunteers and tasks
volunteer_counts = [0,50]#,20,30,40, 50, 60, 70, 80, 90, 100]#, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]
task_counts = [20000]

for level in ['high', 'medium', 'low']:
    for count in volunteer_counts:
        for task_num in task_counts:
            result = run_simulation(level, count, task_num, use_trust=True)
            results.append(result)
            result = run_simulation(level, count, task_num, use_trust=False)
            results.append(result)

# Convert results to a DataFrame
results_df = pd.DataFrame(results)

# Save results to a CSV file
results_df.to_csv("simulation_results5000.csv", index=False)

# Plot settings
levels = ['high', 'medium', 'low']
colors = {'True': 'r', 'False': 'b'}
trustStates = [True, False]

# KPIs to plot
kpis = [
    ('Average latency', 'Average Latency (s)'),
    ('Average task completion time', 'Avg Task Completion Time (s)'),
    ('Task success rate (%)', 'Task Success Rate (%)'),
    ('Task failure rate (%)', 'Task Failure Rate (%)'),
    ('Max queue time', 'Max Queue Time (s)'),
    ('Min queue time', 'Min Queue Time (s)'),
    ('Stddev completion time', 'Stddev Completion Time (s)')
]

fig, axes = plt.subplots(len(kpis), 3, figsize=(22, 25))
fig.suptitle('Simulation Results by Urgency Level and Trust State (Tasks = 20000)')

# Summary dictionary to store which approach is better for each KPI
summary = {level: {kpi[0]: {'Trust Enabled': 0, 'Trust Disabled': 0} for kpi in kpis} for level in levels}

# Loop through each KPI
for kpi_idx, (kpi, ylabel) in enumerate(kpis):
    for i, level in enumerate(levels):
        # Bar width
        width = 0.35
        # X-axis positions for bars
        x_pos = np.arange(len(volunteer_counts))
        # Data for current urgency level
        currentData = results_df[(results_df['Urgency Level'] == level) & (results_df['Number of Tasks'] == 20000)]
        for j, trust in enumerate(trustStates):
            # Filter data for current trust state
            trust_data = currentData[currentData['Trust Enabled'] == trust]
            # Plot the KPI vs. Number of Volunteers as bar chart
            axes[kpi_idx, i].bar(x_pos + (j * width), trust_data[kpi], width=width, color=colors[str(trust)], label=f'Trust {trust}')
            axes[kpi_idx, i].set_xticks(x_pos + width / 2)
            axes[kpi_idx, i].set_xticklabels(volunteer_counts)
            axes[kpi_idx, i].set_title(f'{kpi} - {level} urgency')
            axes[kpi_idx, i].set_xlabel('Number of Volunteers')
            axes[kpi_idx, i].set_ylabel(ylabel)
            axes[kpi_idx, i].legend()

            # Calculate which approach is better for each KPI
            avg_value = trust_data[kpi].mean()
            if trust:
                summary[level][kpi]['Trust Enabled'] = avg_value
            else:
                summary[level][kpi]['Trust Disabled'] = avg_value

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()

# Print summary
print("\nSummary of which approach is better for each KPI:\n")
for level in levels:
    print(f"Urgency Level: {level}")
    for kpi in kpis:
        kpi_name = kpi[0]
        trust_enabled_avg = summary[level][kpi_name]['Trust Enabled']
        trust_disabled_avg = summary[level][kpi_name]['Trust Disabled']
        better_approach = 'Trust Enabled' if trust_enabled_avg < trust_disabled_avg else 'Trust Disabled'
        print(f"  {kpi_name}: {better_approach} (Trust Enabled Avg: {trust_enabled_avg:.2f}, Trust Disabled Avg: {trust_disabled_avg:.2f})")
    print()
