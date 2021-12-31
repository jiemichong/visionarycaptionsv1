from src.domain.viz.shape import Shape


class Circle(Shape):
    def __init__(self, x, y, r):
        self.type = "circle"
        self.x = x
        self.y = y
        self.r = r

    def to_dict(self):
        return {
            'type': self.type,
            'x': self.x,
            'y': self.y,
            'r': self.r
        }