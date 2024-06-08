from Cloud import Cloud
from Edge import Edge
from Volunteer import Volunteer
from LocalDevice import LocalDevice
import numpy as np

class Network:
    def __init__(self, _clouds, _edges, _volunteers, _localDevice):
        self.units = {}
        for unitTypeI in [_clouds, _edges, _volunteers, [_localDevice]]:
            for unitI in unitTypeI:
                self.units[unitI.name] = unitI

    def addUnit(self, _unit):
        self.units[_unit.name] = _unit

    def generateRandomVolunteers(self, _Nvolunteers):
        for volunteerI in range(_Nvolunteers):
            name = 'volunteer_' + str(volunteerI)
            self.generateRandomVolunteer(name)

    def generateRandomVolunteer(self, _name):
        location = np.random.uniform(10, 50)
        CPUspeed = np.random.uniform(1000, 2500)
        bandwidth = np.random.uniform(50, 100)
        latency = np.random.uniform(.001, .01)
        costRate = 'dummyCostRate'
        trust = 1
        availability = 1
        CPUEnergy = np.random.uniform(75, 125)  # Wh
        bandwidthEnergy = np.random.uniform(100, 150)  # Wh per Mbyte

        volunteer_dict = {'name': _name, 'location': location, 'capacity': {'CPUspeed': CPUspeed}, 'costRate': costRate, 'connection': {'bandwidth': bandwidth, 'latency': latency}, 'energy': {'CPUEnergy': CPUEnergy, 'bandwidthEnergy': bandwidthEnergy}}
        volunteer = Volunteer(trust, availability, **volunteer_dict)
        self.addUnit(volunteer)

    def print(self):
        print("\nNetwork structure:")
        for unitNameI in self.units:
            print(unitNameI)
            if self.units[unitNameI].getType() == "volunteer":
                print("\tAvailability = ", self.units[unitNameI].availability)
                print("\tTrust = ", self.units[unitNameI].trust)

def randomNetworkGenerator(_Nclouds, _Nedges):
    clouds = []
    edges = []

    for cloudI in range(_Nclouds):
        name = 'cloud_' + str(cloudI)
        location = np.random.uniform(50, 100)
        CPUspeed = np.random.uniform(3600, 3900)
        bandwidth = np.random.uniform(50, 100)
        latency = np.random.uniform(.01, .08)
        costRate = 'dummyCostRate'

        CPUEnergy = np.random.uniform(100, 150)  # Wh
        bandwidthEnergy = np.random.uniform(175, 225)  # Wh per Mbyte

        cloud_dict = {'name': name, 'location': location, 'capacity': {'CPUspeed': CPUspeed}, 'costRate': costRate, 'connection': {'bandwidth': bandwidth, 'latency': latency}, 'energy': {'CPUEnergy': CPUEnergy, 'bandwidthEnergy': bandwidthEnergy}}
        cloud = Cloud(**cloud_dict)
        clouds.append(cloud)

    for edgeI in range(_Nedges):
        name = 'edge_' + str(edgeI)
        location = np.random.uniform(10, 50)
        CPUspeed = np.random.uniform(2200, 3500)
        bandwidth = np.random.uniform(50, 100)
        latency = np.random.uniform(.001, .01)
        costRate = 'dummyCostRate'
        CPUEnergy = np.random.uniform(75, 150)  # Wh
        bandwidthEnergy = np.random.uniform(150, 200)  # Wh per Mbyte

        edge_dict = {'name': name, 'location': location, 'capacity': {'CPUspeed': CPUspeed}, 'costRate': costRate, 'connection': {'bandwidth': bandwidth, 'latency': latency}, 'energy': {'CPUEnergy': CPUEnergy, 'bandwidthEnergy': bandwidthEnergy}}
        edge = Edge(**edge_dict)
        edges.append(edge)

    CPUspeed = np.random.uniform(1000, 2000)
    bandwidth = np.random.uniform(10, 50)
    latency = 0
    CPUEnergy = np.random.uniform(75, 125)  # Wh
    bandwidthEnergy = np.random.uniform(75, 125)  # Wh per Mbyte
    local_dict = {'capacity': {'CPUspeed': CPUspeed}, 'connection': {'bandwidth': bandwidth, 'latency': latency}, 'energy': {'CPUEnergy': CPUEnergy, 'bandwidthEnergy': bandwidthEnergy}}
    local = LocalDevice(**local_dict)

    return Network(clouds, edges, [], local)


