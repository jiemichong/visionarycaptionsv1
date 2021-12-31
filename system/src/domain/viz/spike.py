class Spike(object):
    def __init__(self, index, height):
        self.index = index
        self.height = height

    def __str__(self):
        return "Spike({self.index}, {self.height})".format(self=self)