from src.domain.text.emphasis import Emphasis
from src.domain.text.properties import Properties

class Caption(object):
    def __init__(self, index: int, start: str, end: str, text: str, properties: Properties):
        self.index = index
        self.start = start
        self.end = end
        self.text = text
        self.properties = properties

    @classmethod
    def from_dict(cls, d):
        properties = Properties([Emphasis.from_dict(emph) for emph in d['properties']['emphasis']])
        return cls(
            index=d['index'],
            start=d['start'],
            end=d['end'],
            text=d['text'],
            properties=properties
        )

    def to_dict(self):
        return {
            'index': self.index,
            'start': self.start,
            'end': self.end,
            'text': self.text,
            'properties': self.properties
        }