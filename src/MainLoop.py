from src.Checkersevaluator import Checkersevaluator
from src.CheckersGame import CheckersGame
from src.Checkersstate import Checkersstate

game = Checkersstate()
game.setStartState()
game.printState()
print(game.getAllMoves())
childStates = game.getAllChildStates()
for i in range(len(childStates)):
    childStates[i].printState()
    nextChildStates = childStates[i].getAllChildStates()
    for j in range(len(nextChildStates)):
        print("\t")
        nextChildStates[j].printState()
    print("\n")
print("Hello, World!")