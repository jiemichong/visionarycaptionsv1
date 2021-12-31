from domain.viz.spike import Spike
from domain.viz.domain import Domain
import numpy as np


class Histogram(object):
    def __init__(self, rectangles):
        self.rectangles = rectangles

    def mode(self) -> Spike:
        heights = [float(rect.height) for rect in self.rectangles]
        idx = np.argmax(heights)
        max_height = heights[idx]
        return Spike(idx, max_height)

    def domain(self) -> Domain:
        xs = [r.x for r in self.rectangles]
        return Domain(min(xs), max(xs))
