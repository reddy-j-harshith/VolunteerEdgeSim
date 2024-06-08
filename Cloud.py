from GeneralUnit import GeneralUnit

class Cloud(GeneralUnit):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def getType(self):
        return 'cloud'
