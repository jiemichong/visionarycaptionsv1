from src.domain.viz.shape import Shape
from src.domain.viz.circle import Circle
from src.domain.viz.rectangle import Rectangle


class Emphasis(object):
    def __init__(self, phrase: str, shape: Shape):
        self.phrase = phrase
        self.shape = shape

    @classmethod
    def from_dict(cls, d):
        if d['shape']['type'] == 'circle':
            shape = Circle(d['shape']['x'], d['shape']['y'], d['shape']['r'])
        elif d['shape']['type'] == 'rectangle':
            shape = Rectangle(d['shape']['x'], d['shape']['y'], d['shape']['w'], d['shape']['h'])
        else:
            shape = Shape()

        return cls(
            phrase=d['phrase'],
            shape=shape
        )

    def to_dict(self):
        return {
            'phrase': self.phrase,
            'shape': self.shape.to_dict()
        }

    def __eq__(self, other):
        return self.phrase == self.phrase and self.shape == self.shape

