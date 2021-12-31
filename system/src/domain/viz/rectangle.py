import re

from src.domain.viz.shape import Shape


class Rectangle(Shape):
    def __init__(self, x: float, y: float, width: float, height: float, transform: str = None):
        self.type = "rectangle"
        self.x_original = x
        self.y_original = y
        self.width = width
        self.height = height
        self.transform = transform

    @property
    def x(self):
        if self.transform:
            result = re.search("translate\((.+)\)", self.transform)
            x_translate = result.group(1).split(',')[0]
            return self.x_original + float(x_translate)
        else:
            return self.x_original

    @property
    def y(self):
        return self.y_original

    def to_dict(self):
        return {
            'type': self.type,
            'x': self.x,
            'y': self.y,
            'w': self.width,
            'h': self.height,
            'transform': self.transform
        }


    def __str__(self):
        return 'Rect({self.x_original}, {self.y_original}, {self.width}, {self.height}, {self.transform})'.format(self=self)

