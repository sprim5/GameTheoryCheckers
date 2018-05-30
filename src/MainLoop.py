from src.Checkersevaluator import Checkersevaluator
from src.CheckersGame import CheckersGame
from src.Checkersstate import Checkersstate

game = Checkersstate()
game.setStartState()
print(game.getAllMoves())
game.printState()
print("Hello, World!")