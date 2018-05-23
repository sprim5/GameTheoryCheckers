class Gamestate:

    def setStartState(self):
        raise NotImplementedError("You should have implemented this")

    def getAllMoves(self):
        raise NotImplementedError("You should have implemented this")

    def possibleMove(self, mv):
        raise NotImplementedError("You should have implemented this")

    def hasNextMove(self):
        raise NotImplementedError("You should have implemented this")

    def getNextMove(self):
        raise NotImplementedError("You should have implemented this")

    def doMove(self, mv):
        raise NotImplementedError("You should have implemented this")

    def undoMove(self, mv):
        raise NotImplementedError("You should have implemented this")

    def getAllChildStates(self):
        raise NotImplementedError("You should have implemented this")

    def hasNextChild(self):
        raise NotImplementedError("You should have implemented this")

    def getNextChild(self):
        raise NotImplementedError("You should have implemented this")

    def getChild(self, mv):
        raise NotImplementedError("You should have implemented this")

    def firstPlayerToMove(self):
        raise NotImplementedError("You should have implemented this")

    def secondPlayerToMove(self):
        raise NotImplementedError("You should have implemented this")

    def isTerminal(self):
        raise NotImplementedError("You should have implemented this")

    def firstPlayerToWin(self):
        raise NotImplementedError("You should have implemented this")

    def secondPlayerToWin(self):
        raise NotImplementedError("Not implemented")

    def draw(self):
        raise NotImplementedError("Not implemented")

    def getMoveHistory(self):
        raise NotImplementedError("Not implemented")

    def getStateHistory(self):
        raise NotImplementedError("Not implemented")