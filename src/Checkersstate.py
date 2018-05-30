from copy import deepcopy

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
        self.genStates = 1
        self.history = []
        self.root = self
        self.stateHistory.append([])


    def getAllMoves(self):
        ls = []
        for y in range(len(self.field)-1):
            for x in range(len(self.field[y]) - 1):
                for tarY in range (5):
                    for tarX in range (5):
                        mv = [[x,y],[tarX+x-2,tarY+y-2]]
                        if self.possibleMove(mv):
                            ls.append(mv)
        return ls

    def possibleMove(self, mv):
        start = mv[0]
        target = mv[1]
        if target[0] == start[0] and target[1] == start[1]:
            return False
        if target[0] < 0 or target[1] < 0 or target[1] >= len(self.field) or target[0] >= len(self.field[target[1]]):
            return False
        if self.field[start[0]][start[1]] == self.currentPlayer and self.field[target[0]][target[1]] == '-':
            if abs(start[0] - target[0]) == 2 or abs(start[1] - target[1]) == 2:
                if (start[0] - target[0] + start[1] - target[1]) % 2 == 0:
                    betweenField = [0,0]
                    if target[0] - start[0] == 2 or target[0] - start[0] == 1:
                        betweenField[0] = 1
                    if target[0] - start[0] == -2 or target[0] - start[0] == -1:
                        betweenField[0] = -1
                    if target[1] - start[1] == 2 or target[1] - start[1] == 1:
                        betweenField[1] = 1
                    if target[1] - start[1] == -2 or target[1] - start[1] == -1:
                        betweenField[1] = -1

                    if self.field[start[0]+betweenField[0]][start[1]+betweenField[1]] != self.currentPlayer and self.field[start[0]+betweenField[0]][start[1]+betweenField[1]] != '-':
                        return True
                    else:
                        return False
                else:
                    return False
                return True
            elif abs(start[0] - target[0]) == 1 or abs(start[1] - target[1]) == 1:
                return True
        return False

    def hasNextMove(self):
        if len(self.getAllMoves()) > 0:
             return True
        else:
             return False

    def getNextMove(self, start):
        pass

    def doMove(self, mv):
        if self.possibleMove(mv):
            self.genStates += 1
            self.history.append(mv)
            self.stateHistory.append(deepcopy(self.history))
            #             print(self.stateHistory)
            start = mv[0]
            target = mv[1]
            self.field[start[0]][start[1]] = '-'
            self.field[target[0]][target[1]] = self.currentPlayer
            if abs(start[0] - target[0]) == 2 or abs(start[1] - target[1]) == 2:
                if (start[0] - target[0] + start[1] - target[1]) % 2 == 0:
                    if self.field[start[0] - target[0]/2][start[1] - target[1]/2] != self.currentPlayer and self.field[start[0] - target[0]/2][start[1] - target[1]/2] != '-':
                        self.field[start[0] - target[0] / 2][start[1] - target[1] / 2] = '-'

            if self.currentPlayer == 'b':
                self.currentPlayer = 'w'
            else:
                self.currentPlayer = 'b'

            if not (self == self.root):
                self.root.genStates += 1
                self.root.stateHistory.append(deepcopy(self.history))

        else:
            raise Exception("Invalid Argument Exception: no possible move")

    def undoMove(self, mv):
        pass

    def getAllChildStates(self):
        mvList = self.getAllMoves()
        childList = []
        n = len(mvList)
        for i in range(n):
            childList.append(self.childState(mvList[i]))
        return childList

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

    def copyState(self):
        gs = Checkersstate()
        field = ()
        currentPlayer = 'w'
        history = []
        root = None
        stateHistory = []
        genStates = 0
        gs.num = self.num
        gs.lastChildMv = self.lastChildMv
        gs.nextChildMv = self.nextChildMv
        gs.currentPlayer = self.currentPlayer
        #        gs.history = deepcopy(self.history)   #deep copy
        gs.history = self.history[:]  # shallow copy
        gs.stateHistory = deepcopy(self.stateHistory)
        gs.root = self.root
        return gs

    def childState(self, mv):
        if self.possibleMove(mv):
            child = self.copyState()
            child.doMove(mv)
            return child
        else:
            return None

    def equalState(self, other):
        if not self.num == other.num:
            return False
        elif not self.lastChildMv == other.lastChildMv:
            return False
        elif not self.nextChildMv == other.nextChildMv:
            return False
        elif not self.firstPlayerToMove == other.firstPlayerToMove:
            return False
        elif not self.equalList(self.history, other.history):
            return False
        else:
            return True

    def printState(self):

        for i in range (len(self.field)):
            out = ""
            for j in range(len(self.field[i])):
                out += self.field[i][j]
            print(out)