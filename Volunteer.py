from GeneralUnit import GeneralUnit
import datetime

class Volunteer(GeneralUnit):
    def __init__(self, _trust, _availability, **kwargs):
        super().__init__(**kwargs)
        self.trust = _trust
        self.availability = _availability
        self.NexecutedTasks = 0
        self.lastShutdownTime = datetime.datetime.now()
        self.successfulTasks = 0
        self.failedTasks = 0
        self.totalLatency = 0.0  # Track latency for trust calculation
        self.totalCompletionTime = 0.0  # Track completion time

    def getType(self):
        return 'volunteer'

    def shutDown(self, _shutDownTime=datetime.datetime.now()):
        self.availability = 0
        self.lastShutdownTime = _shutDownTime
        notExecutedTasksID = []
        for taskI in range(len(self.log['taskIDs'])):
            if self.log['taskEndTime'][taskI] >= _shutDownTime:
                notExecutedTasksID = self.log['taskIDs'][taskI:]
                del self.log['taskIDs'][taskI:]
                del self.log['taskExecutionTime'][taskI:]
                del self.log['taskArrivalTime'][taskI:]
                del self.log['taskEndTime'][taskI:]
                break
        NcurrentExecutedTasks = len(self.log['taskIDs']) - self.NexecutedTasks
        NnotExecutedTasks = len(notExecutedTasksID)
        self.NexecutedTasks = len(self.log['taskIDs'])

        self.trust = self.trust * (NcurrentExecutedTasks + 2) / (NnotExecutedTasks + NcurrentExecutedTasks + 2)
        return notExecutedTasksID

    def turnOn(self):
        self.availability = 1

    def restoreTrust(self):
        self.trust = 0.5

    def updateTrust(self, task):
        if task.successFlag:
            self.successfulTasks += 1
            self.totalLatency += task.getQueingTime().total_seconds()
            self.totalCompletionTime += task.getExecutionTime().total_seconds()
        else:
            self.failedTasks += 1

        # Calculate advanced trust score
        success_rate = self.successfulTasks / (self.successfulTasks + self.failedTasks + 1)
        avg_latency = self.totalLatency / (self.successfulTasks + 1)
        avg_completion_time = self.totalCompletionTime / (self.successfulTasks + 1)
        self.trust = 0.5 * success_rate + 0.25 * (1 / (1 + avg_latency)) + 0.25 * (1 / (1 + avg_completion_time))
