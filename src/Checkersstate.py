from copy import deepcopy

from src.Evaluator import Evaluator
from src.Gamestate import Gamestate
class Checkersstate(Gamestate):


    field = ()
    currentPlayer = 'w'
    history = []
    root = None
    stateHistory = []
    genStates = 0
    depth = 0


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
        evalu = Checkersevaluator()
        self.heuristicValue = evalu.heuristicValue(self)
        self.stateHistory.append([])


    def getAllMoves(self):
        ls = []
        for y in range(len(self.field)):
            for x in range(len(self.field[y])):
                for tarY in range (0,6):
                    for tarX in range (0,6):
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
            self.depth += 1
            self.history.append(mv)
            self.stateHistory.append(deepcopy(self.history))
            #             print(self.stateHistory)
            start = mv[0]
            target = mv[1]
            self.field[start[0]][start[1]] = '-'
            self.field[target[0]][target[1]] = self.currentPlayer
            # if abs(start[0] - target[0]) == 2 or abs(start[1] - target[1]) == 2:
            #     if (start[0] - target[0] + start[1] - target[1]) % 2 == 0:
            #         if self.field[start[0] - target[0]/2][start[1] - target[1]/2] != self.currentPlayer and self.field[start[0] - target[0]/2][start[1] - target[1]/2] != '-':
            #             self.field[start[0] - target[0] / 2][start[1] - target[1] / 2] = '-'

            if abs(start[0] - target[0]) == 2 or abs(start[1] - target[1]) == 2:
                betweenField = [0, 0]
                if target[0] - start[0] == 2 or target[0] - start[0] == 1:
                    betweenField[0] = 1
                if target[0] - start[0] == -2 or target[0] - start[0] == -1:
                    betweenField[0] = -1
                if target[1] - start[1] == 2 or target[1] - start[1] == 1:
                    betweenField[1] = 1
                if target[1] - start[1] == -2 or target[1] - start[1] == -1:
                    betweenField[1] = -1

                if self.field[start[0] + betweenField[0]][start[1] + betweenField[1]] != self.currentPlayer and self.field[start[0] + betweenField[0]][start[1] + betweenField[1]] != '-':
                    self.field[start[0] + betweenField[0]][start[1] + betweenField[1]] = '-'

            if self.currentPlayer == 'b':
                self.currentPlayer = 'w'
            else:
                self.currentPlayer = 'b'

            evalu = Checkersevaluator()
            self.heuristicValue = evalu.heuristicValue(self)
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
        gs.field = deepcopy(self.field)
        gs.currentPlayer = self.currentPlayer
        gs.history = deepcopy(self.history)   #deep copy
        gs.depth = self.depth
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

    def printState(self):
        print(self.currentPlayer)
        print(self.heuristicValue)
        print(self.depth)
        print(self.history)
        print(self.root)
        print(self.stateHistory)
        for i in range (len(self.field)):
            out = ""
            for j in range(len(self.field[i])):
                out += self.field[i][j]
            print(out)

    def looseCondition(self):
        return self.hasNextMove() == False

    def heuristicMinimax(self, depth, factor):
        childStates = self.getAllChildStates()
        nextChild = 0
        bestHeuristic = -1000

        if depth == 0:
            for i in range(len(childStates)):
                if childStates[i].heuristicValue * factor > bestHeuristic:
                    nextChild = i
                    bestHeuristic = childStates[i].heuristicValue * factor

            return childStates[nextChild]
        else:
            for i in range(len(childStates)):
                value = childStates[i].heuristicMinimax(depth-1, factor*(-1)).heuristicValue
                if  value * factor > bestHeuristic:
                    nextChild = i
                    bestHeuristic = value * factor
                childStates[i].heuristicValue = value
            return childStates[nextChild]

class Checkersevaluator(Evaluator):
    fieldValues =   ([5, 3, 3, 3, 5],
                     [3, 0, 0, 0, 3],
                     [3, 0, 0, 0, 3],
                     [3, 0, 0, 0, 3],
                     [5, 3, 3, 3, 5]
                     )

    def heuristicValue(self, gs):
        if not (isinstance(gs, Checkersstate)):
             raise Exception("Illegal Argument")
        else:
            whiteValue = 0
            blackValue = 0
            for y in range(len(gs.field)):
                for x in range(len(gs.field[y])):
                    if gs.field[y][x] == 'w':
                        whiteValue += 8
                        whiteValue += self.getFieldValue(x,y)
                    elif gs.field[y][x] == 'b':
                        blackValue += 8
                        blackValue += self.getFieldValue(x, y)
            return whiteValue - blackValue


    def getMinValue(self):
        return -1

    def getMaxValue(self):
        return 1

    def exactValue(self, gs):
        pass

    def evaluate(self, gs):
        pass

    def getFieldValue(self, x, y,):
        return self.fieldValues[x][y]