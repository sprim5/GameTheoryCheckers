class Evaluator:

    def heuristicValue(self, gs):
        raise NotImplementedError("Not implemented")

    def simpleHeuristicValue(self, gs):
        raise NotImplementedError("Not implemented")

    def getMinValue(self):
        raise NotImplementedError("Not implemented")

    def getMaxValue(self):
        raise NotImplementedError("Not implemented")

    def exactValue(self, gs):
        raise NotImplementedError("Not implemented")

    def evaluate(self, gs):
        raise NotImplementedError("Not implemented")