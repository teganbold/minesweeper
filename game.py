import pygame

class Game():
    def __init__(self, board: object, screensize: tuple) -> None:
        self.title = "Minesweeper"
        self.board = board
        self.screensize = screensize
        self.screen = pygame.display.set_mode(self.screensize)
        self.game_over = False

    def run(self) -> None:
        pygame.init()
        pygame.display.set_caption("Minesweeper")
        run_game = True
        while run_game == True:
            # pygame.time.Clock().tick(self.fps)
            pygame.display.update()
            self.drawBoard()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run_game = False
                if event.type == pygame.MOUSEBUTTONDOWN and not self.game_over:
                    pos = pygame.mouse.get_pos()
                    piece = self.board.handleClick(pos)
                    if event.button == 1 and not piece.getFlagged():
                        self.clickPiece(piece)
                    elif event.button == 3 and not piece.isClicked():
                        piece.flagPiece()


    def drawBoard(self) -> None:
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

    def getImage(self, piece: str) -> str:
        dir = "assets/"
        if self.game_over and piece.hasMine() and not piece.isClicked():
            return f"{dir}unclicked-bomb.png"
        if piece.getFlagged():
            return f"{dir}flag.png"
        if not piece.isClicked():
            return f"{dir}unclicked.png"
        if piece.hasMine():
            return f"{dir}bomb-at-clicked-block.png"
        return f"{dir}{piece.getNeighbors()}.png"

    def clickPiece(self, piece) -> None:
        piece.click()
        # recursively click piece if 0 neighboring bombs
        if piece.getNeighbors() == 0 and not piece.hasMine():
            x = piece.getRow()
            y = piece.getCol()
            board_size = self.board.getBoardSize()
            for r in range(max(0, x - 1), min(board_size[0] -1, x + 1)+1):
                for c in range(max(0, y - 1), min(board_size[1] - 1, y + 1)+1):
                    piece = self.board.getBoard()[r][c]
                    if not piece.isClicked():
                        self.clickPiece(piece)
        if piece.hasMine():
            self.game_over = True
