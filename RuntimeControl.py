class RuntimeControl:
    def __init__(self):
        self.assignedTasks = []
        self.units = []
        self.taskIndex = []
        self.notAssignedTasks = []

    def appendAssignedTask(self, _task, _device):
        self.assignedTasks.append(_task)
        self.units.append(_device)
        self.taskIndex.append(tuple([_task.id, len(self.assignedTasks)]))

    def appendNotAssignedTask(self, _task):
        self.notAssignedTasks.append(_task)

    def restart(self):
        self.assignedTasks = []
        self.units = []
        self.taskIndex = []
        self.notAssignedTasks = []

    def print(self):
        print("Runtime control:")
        print("\n**************************")
        print("Assigned tasks:\n")
        unitI = 0
        for taskI in self.assignedTasks:
            print("Task ID = ", taskI.id)
            print("Assigned to unit: ", self.units[unitI])
            print("Arrival time = ", taskI.arrivalTime)
            print("StartTime = ", taskI.startTime)
            print("EndTime = ", taskI.endTime)
            print("Assigned %d times" % taskI.assignmentCounter)
            print("\n")
            unitI = unitI + 1

        print("\n**************************")
        print("Not assigned tasks:\n")
        for taskI in self.notAssignedTasks:
            print("Task ID = ", taskI.id)
            print("Assigned %d times" % taskI.assignmentCounter)
            print("\n")

    def getNotAssignedTasks(self):
        return len(self.notAssignedTasks)
