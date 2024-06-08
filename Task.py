import datetime
import numpy as np

class Task:
    __slots__ = ['id', 'type', 'priority', 'arrivalTime', 'deadlineTime',
                 'delayTolerance', 'CPUcycles', 'memorySize', 'incentive',
                 'startTime', 'endTime', 'wastedTime',
                 'assignedUnit', 'successFlag', 'assignmentCounter']

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.wastedTime = datetime.timedelta(seconds=0.0)
        self.successFlag = True
        self.assignmentCounter = 0

    def setArrivalTime(self, _arrival):
        self.arrivalTime = _arrival

    def setStartTime(self, _start):
        self.startTime = _start

    def setEndTime(self, _end):
        self.endTime = _end

    def setUnitName(self, _name):
        self.assignedUnit = _name

    def assign(self, _startTime, _endTime, _unitName):
        self.assignmentCounter = self.assignmentCounter + 1
        self.setStartTime(_startTime)
        self.setEndTime(_endTime)
        self.setUnitName(_unitName)

    def notAssigned(self):
        self.successFlag = False
        self.endTime = datetime.datetime(1, 1, 1, 0, 0)
        self.assignedUnit = "None"

    def prepareForReassignment(self, _reassignmentTime):
        self.wastedTime = self.wastedTime + _reassignmentTime - self.arrivalTime
        self.arrivalTime = _reassignmentTime
        self.assignedUnit = "None"
        self.startTime = None
        self.endTime = None

    def getExecutionTime(self):
        if self.assignedUnit == "None":
            raise TypeError("Cannot call this function because this task was not assigned")
        return self.endTime - self.startTime

    def getQueuingTime(self):
        if self.assignedUnit == "None":
            raise TypeError("Cannot call this function because this task was not assigned")
        return self.startTime - self.arrivalTime + self.wastedTime

    def print(self):
        print('\nTask ID = ', self.id)
        print('Arrival time = ', self.arrivalTime - self.wastedTime)
        print('Start time = ', self.startTime)
        print('Queuing time = ', self.getQueuingTime(), 's')
        print('Execution time = ', self.getExecutionTime(), 's')
        print('End time = ', self.endTime)
        print('Assigned unit = ', self.assignedUnit)
        print('Success = ', self.successFlag)

def randomTaskGenerator(_Ntasks):
    tasks = []
    for taskI in range(_Ntasks):
        priority = np.random.uniform(0, 20)
        delayTolerance = np.random.uniform(0, 1)
        incentive = np.random.uniform(0.1, 1)
        minDeadline = 60 * 5  # [s]
        maxDeadline = 60 * 40  # [s]
        deadlineTime = np.random.uniform(minDeadline, maxDeadline)
        CPUcycles = np.random.uniform(deadlineTime / 10 * 1000,
                                      deadlineTime / 2 * 1000)
        memorySize = np.random.uniform(1, 10)
        arrivalTime = datetime.datetime.now() + \
            datetime.timedelta(seconds=np.random.uniform(0, simulationLength))
        deadlineTime = arrivalTime + \
            datetime.timedelta(seconds=deadlineTime)

        task_dict = {'id': taskI, 'type': 'imageProcessing', 'priority': priority,
                     'arrivalTime': arrivalTime,
                     'deadlineTime': deadlineTime,
                     'delayTolerance': delayTolerance,
                     'CPUcycles': CPUcycles, 'memorySize': memorySize,
                     'incentive': incentive}

        task = Task(**task_dict)
        tasks.append(task)
    return tasks
