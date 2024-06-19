import pygame
import random
from piece import Piece

class Board():
    def __init__(self, board_size, mine_probablility, screen_size) -> None:
        self.board_size = board_size
        self.board = []
        self.piece_size = (screen_size[0] // board_size[0], screen_size[0] // board_size[0])
        self.createBoard(mine_probablility)

    def createBoard(self, mine_probablility):
        for rows in range(self.board_size[0]):
            row = []
            for cols in range(self.board_size[1]):
                piece = Piece(self.plantMine(mine_probablility))
                row.append(piece)
            self.board.append(row)

    def plantMine(self, mine_probablility):
        if random.random() < mine_probablility:
            return True
        return False
    
    def handleClick(self, pos):
        print(pos)
        index = (pos[0] // self.piece_size[0], pos[1] // self.piece_size[1])
        print(index)
        print(self.getPiece(index).getHasMine())

    def getPiece(self, index):
        return self.board[index[0]][index[1]]

    def getBoard(self):
        return self.board

    def getBoardSize(self):
        return self.board_size
