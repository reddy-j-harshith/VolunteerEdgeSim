from GeneralUnit import GeneralUnit

class Edge(GeneralUnit):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def getType(self):
        return 'edge'
