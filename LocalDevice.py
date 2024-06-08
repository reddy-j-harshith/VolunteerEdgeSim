from GeneralUnit import GeneralUnit

class LocalDevice(GeneralUnit):
    def __init__(self, **kwargs):
        kwargs['name'] = "myDevice"
        kwargs['location'] = 0
        kwargs['costRate'] = 0
        super().__init__(**kwargs)

    def getType(self):
        return 'localDevice'
