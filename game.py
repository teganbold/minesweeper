import pygame
from pygame.locals import *

class Game():
    def __init__(self, board, screensize) -> None:
        self.title = "Minesweeper"
        self.fps = 60
        self.board = board
        self.screensize = screensize
        self.screen = pygame.display.set_mode(self.screensize)
        self.game_over = False

    def run(self):
        pygame.init()
        pygame.display.set_caption("Minesweeper")
        run_game = True
        while run_game == True:
            pygame.time.Clock().tick(self.fps)
            pygame.display.update()
            self.drawBoard()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run_game = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.clickPiece()
            if self.game_over:
                #Print the whole board:
                pass
        
    def drawBoard(self):
        top_left = (0, 0)
        for row in self.board.getBoard():
            for piece in row:
                image = pygame.image.load(self.getImage(piece))
                board_size = self.board.getBoardSize()
                piece_size = (self.screensize[0] // board_size[0], self.screensize[0] // board_size[0])
                image = pygame.transform.scale(image, piece_size)
                self.screen.blit(image, top_left)
                top_left = (top_left[0] + piece_size[0],  top_left[1])
            top_left = (0, top_left[1] + piece_size[1])
    
    def getImage(self, piece):
        dir = "assets/"
        if not piece.isClicked():
            return f"{dir}unclicked.png"
        if piece.hasMine():
            return f"{dir}bomb-at-clicked-block.png"
        return f"{dir}{piece.getNeighbors()}.png"
        
    def clickPiece(self):
        pos = pygame.mouse.get_pos()
        piece = self.board.handleClick(pos)
        piece.click()
        if piece.hasMine():
            self.game_over = True
