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
                piece = Piece(self.plantMine(mine_probablility), rows, cols)
                row.append(piece)
            self.board.append(row)
        self.getNeighbors()

    def plantMine(self, mine_probablility):
        if random.random() < mine_probablility:
            return True
        return False
    
    def getNeighbors(self):
        for row in self.board:
            for piece in row:
                x = piece.getRow()
                y = piece.getCol()
                piece.setNeighbors(self.populateNeighbors(x, y))

    def populateNeighbors(self, x, y):
        neighbors = 0
        # Check All the Neighbors
        for r in range(max(0, x - 1), min(self.board_size[0] -1, x + 1)+1):
            for c in range(max(0, y - 1), min(self.board_size[1] - 1, y + 1)+1):
                if x == r and y == c: #Skip original Value
                    continue
                if self.board[r][c].hasMine():
                    neighbors += 1
        return neighbors

    def handleClick(self, pos):
        index = (pos[1] // self.piece_size[1], pos[0] // self.piece_size[0])
        return self.getPiece(index)

    def getPiece(self, index):
        return self.board[index[0]][index[1]]

    def getBoard(self):
        return self.board

    def getBoardSize(self):
        return self.board_size
