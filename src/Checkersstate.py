from src.Gamestate import Gamestate
class Checkersstate(Gamestate):

    field = ()
    currentPlayer = 'w'
    history = []
    root = None
    stateHistory = []
    genStates = 0

    def setStartState(self):
        self.field = (['w', 'w', 'w', 'w', 'w'],
                      ['w', 'w', 'w', 'w', 'w'],
                      ['w', 'w', '-', 'b', 'b'],
                      ['b', 'b', 'b', 'b', 'b'],
                      ['b', 'b', 'b', 'b', 'b']
                     )


    def getAllMoves(self):
        ls = []
        while self.hasNextMove():
            ls.append(self.getNextMove())
        return ls

    def possibleMove(self, mv):
        start = mv[0]
        target = mv[1]
        if self.field[start[0]][start[1]] == self.currentPlayer and self.field[target[0]][target[1]] == '-':
            if abs(start[0] - target[0]) == 2 or abs(start[1] - target[1]) == 2:
                if (start[0] - target[0] + start[1] - target[1]) % 2 == 0:
                    
                return True
            elif abs(start[0] - target[0]) == 1 or abs(start[1] - target[1]) == 1:
                return True
        return False

    def hasNextMove(self):
        pass

    def getNextMove(self):
        pass

    def doMove(self, mv):
        pass

    def undoMove(self, mv):
        pass

    def getAllChildStates(self):
        pass

    def hasNextChild(self):
        pass

    def getNextChild(self):
        pass

    def getChild(self, mv):
        pass

    def firstPlayerToMove(self):
        return self.firstPlayerToMove

    def secondPlayerToMove(self):
        return not self.firstPlayerToMove

    def isTerminal(self):
        pass

    def firstPlayerToWin(self):
        pass

    def secondPlayerToWin(self):
        pass

    def draw(self):
        pass

    def getMoveHistory(self):
        return self.history  # without copy

    def getStateHistory(self):
        return self.stateHistory  # without copy