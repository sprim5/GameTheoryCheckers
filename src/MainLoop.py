from src.Checkersstate import Checkersstate

game = Checkersstate()
game.setStartState()
game.printState()
print(game.getAllMoves())
# childStates = game.getAllChildStates()


while (game.looseCondition() == False):
    childStates = game.getAllChildStates()
    nextChild = 0
    for i in range(len(childStates)):
        if game.currentPlayer == 'w':
            if childStates[i].heuristicValue > childStates[nextChild].heuristicValue:
                nextChild = i
        else:
            if childStates[i].heuristicValue < childStates[nextChild].heuristicValue:
                nextChild = i
    childStates[nextChild].printState()
    print("\n")
    game = childStates[nextChild]
print("Hello, World!")

