#
import copy

from s5_Alice_Bob.ISTR import InputSemanticTransitionRelation

class ISS(ISTR):
    def __init__(self, program):
        self.program = program

    def initial(self):
        return [self.program.init]

    def enabledActions(self, input, source):
        return filter(lambda r : r.guard(input, source), self.program.rules)

    def execute(self, action, input, source):
        target = copy.deepcopy(source)
        n = action(input, target)
        return [target]
