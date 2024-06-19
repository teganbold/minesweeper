import pygame

class Board():
    def __init__(self, board_size) -> None:
        self.board_size = board_size
        self.board = []
        self.createBoard()

    def createBoard(self):
        for rows in range(self.board_size[0]):
            row = []
            for cols in range(self.board_size[1]):
                piece = []
                row.append(piece)
            self.board.append(row)

    def getBoard(self):
        return self.board

    def getBoardSize(self):
        return self.board_size
