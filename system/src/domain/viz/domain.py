class Domain(object):
    def __init__(self, _min, _max):
        self.min = _min
        self.max = _max

    def __str__(self):
        return "Domain({self.min}, {self.max})".format(self=self)


def project(value: float, domain_1: Domain, domain_2: Domain) -> float:
    """project a value on domain_1 to a value on domain_2"""
    r = (value - domain_1.min) / (domain_1.max - domain_1.min)
    ret = (domain_2.max - domain_2.min) * r + domain_2.min
    return ret