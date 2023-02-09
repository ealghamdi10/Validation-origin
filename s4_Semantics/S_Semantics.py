import copy

from s4_Semantics.Semantic_T_R import SemanticTransitionRelation


class SoupSemantics(SemanticTransitionRelation):
    def __init__(self, program):
        self.program = program

    def initialConfigurations(self):
        return [self.program.ini]

    def enabledActions(self, source):
        return filter(lambda r: r.guard(source), self.program.rules)

    def execute(self, action, source):
        t=source.copy()
        return action.execute(t) 