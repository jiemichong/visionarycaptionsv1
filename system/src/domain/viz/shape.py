import abc
from abc import ABC

# pip install -e .


class Shape(ABC):

    @abc.abstractmethod
    def to_dict(self):
        return {}

    