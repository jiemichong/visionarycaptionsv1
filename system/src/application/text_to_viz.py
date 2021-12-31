from domain.viz.domain import Domain, project
from domain.text.operator_lang import OperatorLang, Peak, MoreThan, LessThan, NoOp


class TextToViz(object):
    def __init__(self, phrases, histogram):
        self.phrases = phrases
        self.histogram = histogram
        self.viz_domain = self.histogram.domain()
        self.phrase_min = 0
        self.phrase_max = 3000
        self.phrase_domain = Domain(self.phrase_min, self.phrase_max)

    def run(self):
        for phrase in self.phrases:
            op = self.phrase_to_op(phrase)

            if type(op) is Peak:
                spike = self.histogram.mode()
                print(op, op.value)

                print("KH: I'm not sure if this is the coordinate that we want to plot.", self.project(op.value), spike.height)
                print("Carmen: need a radius. Maybe something like bar width * 3")
            elif type(op) is MoreThan:
                print(op, op.value)

                print("KH: Is this the x-range that we want to plot for 'more than'?", self.project(op.value), self.project(self.phrase_max))
                print("Carmen: OK-ish.")
            elif type(op) is LessThan:
                print(op, op.value)

                print("KH: Is this the x-range that we want to plot for 'less than'?", self.project(self.phrase_min), self.project(op.value))
                print("Carmen: x should starts around 542. width should be around 490")
            print()


        return

    def project(self, value):
        return project(value, self.phrase_domain, self.viz_domain)

    def phrase_to_op(self, phrase) -> OperatorLang:
        if Peak.match(phrase):
            op = Peak(phrase)
        elif MoreThan.match(phrase):
            op = MoreThan(phrase)
        elif LessThan.match(phrase):
            op = LessThan(phrase)
        else:
            op = NoOp(phrase)
        return op
