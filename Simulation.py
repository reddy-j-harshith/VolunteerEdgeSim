from Network import Network
from Task import Task
from RuntimeControl import RuntimeControl
import datetime
import random
import numpy as np
import pandas as pd
import plotly.express as px

def taskSorting(_task):
    return _task.arrivalTime.timestamp()

class Simulation:
    def __init__(self, _network, _tasks, _optimizationGoal):
        self.network = _network
        self.tasks = _tasks
        self.tasks.sort(key=taskSorting)
        self.optimizationGoal = _optimizationGoal
        self.runtimeControl = RuntimeControl()
        self.notAssignedTasks = []

    def getBestDevice(self, _task):
        executionTimeMin = _task.arrivalTime + datetime.timedelta(days=10000)  # Just a big number
        bestDevice = 'None'
        success = False
        startTime = None
        for unitI in self.network.units:
            if self.network.units[unitI].getType() == "volunteer":
                if self.network.units[unitI].availability == 0:
                    continue
                else:
                    if self.volunteerTrustCheck(unitI, _task.arrivalTime) == 0:
                        continue
            exeT = self.network.units[unitI].computeExecutionTime(_task)
            startTime = max(self.network.units[unitI].endTime, _task.arrivalTime)
            endTime = startTime + exeT
            if _task.deadlineTime > endTime:
                if endTime < executionTimeMin:
                    executionTimeMin = endTime
                    bestDevice = unitI
                    success = True
        return bestDevice, success

    def volunteerTrustCheck(self, _unitName, _currentTime):
        flag = 1
        if self.network.units[_unitName].trust < volunteerTrustTreshold:
            if self.network.units[_unitName].getUntrustedTime(_currentTime) > volunteerTimeoutTreshold:
                self.network.units[_unitName].restoreTrust()
            flag = 0
        return flag

    def shutDownVolunteer(self, _volunteerName, _shutDownTime):
        toReassignTasksIDs = self.network.units[_volunteerName].shutDown(_shutDownTime)
        for taskID in toReassignTasksIDs:
            task = [x for x in self.tasks if x.id == taskID][0]
            task.prepareForReassignment(_shutDownTime)
            bestDevice, success = self.getBestDevice(task)
            if success:
                self.network.units[bestDevice].assignTask(task)
                self.runtimeControl.appendAssignedTask(task, bestDevice)
            else:
                self.runtimeControl.appendNotAssignedTask(task)
                task.notAssigned()

    def run(self):
        self.runtimeControl.restart()

        for taskI in self.tasks:
            bestDevice, success = self.getBestDevice(taskI)
            if success:
                self.network.units[bestDevice].assignTask(taskI)
                if self.network.units[bestDevice].getType() == "volunteer":
                    self.network.units[bestDevice].updateTrust(taskI)
                self.runtimeControl.appendAssignedTask(taskI, bestDevice)
            else:
                self.runtimeControl.appendNotAssignedTask(taskI)
                taskI.notAssigned()
        return self.runtimeControl

    def runWithShutdown(self):
        self.runtimeControl.restart()
        for taskI in self.tasks:
            if taskI.id == 2:
                self.network.units["volunteer_1"].turnOn()
            bestDevice, success = self.getBestDevice(taskI)
            if success:
                self.network.units[bestDevice].assignTask(taskI)
                if self.network.units[bestDevice].getType() == "volunteer":
                    self.network.units[bestDevice].updateTrust(taskI)
                self.runtimeControl.appendAssignedTask(taskI, bestDevice)
            else:
                self.runtimeControl.appendNotAssignedTask(taskI)
                taskI.notAssigned()
            if taskI.id == 1:
                shutDownTime = taskI.arrivalTime
                print("\nVolunteer log")
                print(self.network.units["volunteer_1"].printLog())
                print("\nShutDown time = ", shutDownTime)
                self.shutDownVolunteer("volunteer_1", shutDownTime)
                print("\nVolunteer log after shutDown")
                print(self.network.units["volunteer_1"].printLog())
        return self.runtimeControl

    def runWithRandomShutdowns(self, _shutDownFreq, _turnOnFreq):
        self.runtimeControl.restart()
        for taskI in self.tasks:
            if taskI.id % _shutDownFreq == 1:
                shutDownTime = taskI.arrivalTime
                activeVolunteers = self.getActiveVolunteers()
                if len(activeVolunteers) != 0:
                    self.shutDownVolunteer(random.choice(activeVolunteers), shutDownTime)
            bestDevice, success = self.getBestDevice(taskI)
            if success:
                self.network.units[bestDevice].assignTask(taskI)
                if self.network.units[bestDevice].getType() == "volunteer":
                    self.network.units[bestDevice].updateTrust(taskI)
                self.runtimeControl.appendAssignedTask(taskI, bestDevice)
            else:
                self.runtimeControl.appendNotAssignedTask(taskI)
                taskI.notAssigned()
            if (taskI.id + 3) % _turnOnFreq == 1:
                notActiveVolunteers = self.getNotActiveVolunteers()
                if len(notActiveVolunteers) != 0:
                    self.network.units[random.choice(notActiveVolunteers)].turnOn()
        return self.runtimeControl

    def getActiveVolunteers(self):
        activeVolunteers = []
        for unitI in self.network.units:
            if self.network.units[unitI].getType() == "volunteer":
                if self.network.units[unitI].availability == 1:
                    activeVolunteers.append(self.network.units[unitI].name)
        return activeVolunteers

    def getNotActiveVolunteers(self):
        notActiveVolunteers = []
        for unitI in self.network.units:
            if self.network.units[unitI].getType() == "volunteer":
                if self.network.units[unitI].availability == 0:
                    notActiveVolunteers.append(self.network.units[unitI].name)
        return notActiveVolunteers

    def plotGanttChart(self):
        tasks_list = []
        for taskI in self.tasks:
            if taskI.assignedUnit != "None":
                tasks_list.append(dict(Unit=taskI.assignedUnit, TaskID=taskI.id, Start=taskI.startTime, Finish=taskI.endTime))
        df = pd.DataFrame(tasks_list)
        fig = px.timeline(df, x_start="Start", x_end="Finish", y="Unit", color="TaskID")
        fig.update_yaxes(autorange="reversed")
        fig.show()

    def totalTasksDelay(self):
        tasksDelay = 0
        for taskI in self.tasks:
            if taskI.assignedUnit != "None":
                tasksDelay = tasksDelay + (taskI.endTime - taskI.arrivalTime + taskI.wastedTime).total_seconds()
        return tasksDelay
