from src.Checkersstate import Checkersstate

# game = Checkersstate()
# game.setStartState()
# game.printState()
# childStates = game.getAllChildStates()


# while (game.looseCondition() == False):
#     childStates = game.getAllChildStates()
#     nextChild = 0
#     for i in range(len(childStates)):
#         if game.currentPlayer == 'w':
#             if childStates[i].heuristicValue > childStates[nextChild].heuristicValue:
#                 nextChild = i
#         else:
#             if childStates[i].heuristicValue < childStates[nextChild].heuristicValue:
#                 nextChild = i
#     childStates[nextChild].printState()
#     print("\n")
#     game = childStates[nextChild]

print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
game = Checkersstate()
game.setStartState()
game.printState()
while (game.looseCondition() == False):
    if game.currentPlayer == 'w':
        nextChild = game.heuristicMinimax(3, 1)
    else:
        nextChild = game.heuristicMinimax(3, -1)
    nextChild.printState()
    print("\n")
    game = nextChild

