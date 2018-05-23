class CheckersGame:
    """A simple example class"""
    gameBoard = ()

    def __init__(self):
        self.gameBoard = (['w', 'w', 'w', 'w', 'w'],
                     ['w', 'w', 'w', 'w', 'w'],
                     ['w', 'w', '-', 'b', 'b'],
                     ['b', 'b', 'b', 'b', 'b'],
                     ['b', 'b', 'b', 'b', 'b']
                     )


    def printGameBoard(self):

        for i in range (len(self.gameBoard)):
            out = ""
            for j in range(len(self.gameBoard)):
                out += self.gameBoard[i][j]
            print(out)