class Properties(object):
    def __init__(self, emphases):
        self.emphases = emphases

    def to_dict(self):
        return {
            'emphasis': self.emphases
        }

    def __eq__(self, other):
        return self.emphases == other.emphases

