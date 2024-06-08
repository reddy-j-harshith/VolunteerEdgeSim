import datetime
import numpy as np

class GeneralUnit:
    __slots__ = ['name', 'location', 'capacity', 'costRate', 'connection', 'energy']

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.transmissionPower = 10  # [dBm]
        self.transmissionPower = 10 ** (self.transmissionPower / 10)  # [mW]
        self.fadingCoeff = 0.7
        self.noisePower = 0.008 * self.transmissionPower * self.fadingCoeff ** 2  # [mW]
        self.pathLossExponent = 2.5

        # The endTime of a unit is the time at which it finished its last job
        self.endTime = datetime.datetime.now()
        self.log = {'taskIDs': [], 'taskExecutionTime': [], 'taskArrivalTime': [], 'taskEndTime': []}

    def computeExecutionTime(self, _task, considerEnergy=True):
        computationTime = _task.CPUcycles / self.capacity['CPUspeed']
        dataTransferTime = 0
        if self.getType() != "myDevice":
            dataTransferTime = _task.memorySize / self.connection['bandwidth'] + self.connection['latency']

        totalEnergy = 0

        if considerEnergy:
            computationEnergy = computationTime * self.energy['CPUEnergy'] / 3600
            dataTransferEnergy = 0
            if self.getType() != "myDevice":
                dataTransferEnergy = _task.memorySize * self.energy['bandwidthEnergy'] * dataTransferTime / 3600

            totalEnergy = dataTransferEnergy + computationEnergy

        totalEnergy = transitionCoefficient * totalEnergy
        return datetime.timedelta(seconds=computationTime + dataTransferTime + self.getWirelessTransferTime(_task.memorySize) + totalEnergy)

    def getWirelessTransferTime(self, _taskMemorySize):
        wirelessTransferTime = 0  # [s]
        if self.location > 0.0:
            wirelessTransferTime = self.connection['bandwidth'] * np.log2(
                1 + (self.transmissionPower * self.fadingCoeff ** 2) / (self.noisePower * self.location ** self.pathLossExponent))
        return wirelessTransferTime

    def assignTask(self, _task):
        execTime = self.computeExecutionTime(_task)
        if self.endTime < _task.arrivalTime:  # unit queue is empty
            self.endTime = _task.arrivalTime + execTime
        else:  # the tasks goes in the queue
            self.endTime = self.endTime + execTime

        taskStartTime = self.endTime - execTime
        _task.assign(taskStartTime, self.endTime, self.name)
        if _task.endTime <= _task.startTime:
            raise TypeError("The task computation of exeTime went wrong")

        self.append2log(_task.id, _task.getExecutionTime(), _task.arrivalTime, _task.endTime)

    def append2log(self, _taskID, _taskExecutionTime, _taskArrivalTime, _taskEndTime):
        self.log['taskIDs'].append(_taskID)
        self.log['taskExecutionTime'].append(_taskExecutionTime)
        self.log['taskArrivalTime'].append(_taskArrivalTime)
        self.log['taskEndTime'].append(_taskEndTime)

    def printLog(self):
        print("Log of unit: ", self.name)
        print("Unit type: ", self.getType())
        print("Assigned tasks: ", self.log['taskIDs'])

    def getType(self):
        return 'General unit'
