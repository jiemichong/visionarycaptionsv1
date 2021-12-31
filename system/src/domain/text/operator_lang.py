class OperatorLang(object):
    keywords = []

    def __init__(self):
        pass

    @classmethod
    def match(cls, phrase):
        return any([keyword in phrase for keyword in cls.keywords])


class NoOp(OperatorLang):
    def __init__(self, phrase):
        self.phrase = phrase

    def __str__(self):
        return "NoOp({self.phrase})".format(self=self)


class LessThan(OperatorLang):
    keywords = ["fewer"]

    @property
    def value(self):
        digits = [float(s) for s in self.phrase.split() if s.isdigit()]
        return max(digits)

    def __init__(self, phrase):
        self.phrase = phrase

    def __str__(self):
        return "LessThan({self.phrase})".format(self=self)


class MoreThan(OperatorLang):
    keywords = ["more"]

    @property
    def value(self):
        digits = [float(s) for s in self.phrase.split() if s.isdigit()]
        return max(digits)

    def __init__(self, phrase):
        self.phrase = phrase

    def __str__(self):
        return "MoreThan({self.phrase})".format(self=self)



class Peak(OperatorLang):
    keywords = ["spike", "max", "mode"]

    @property
    def value(self):
        digits = [float(s) for s in self.phrase.split() if s.isdigit()]
        return digits[0]

    def __init__(self, phrase):
        self.phrase = phrase

    def __str__(self):
        return "Peak({self.phrase})".format(self=self)