class Piece():
    def __init__(self, has_mine: bool, row: int, col: int) -> None:
        self.has_mine = has_mine
        self.is_clicked = False
        self.flagged = False
        self.row = row
        self.col = col
        self.neighbors = 0

    def hasMine(self) -> bool:
        return self.has_mine

    def click(self) -> None:
        self.is_clicked = True

    def isClicked(self) -> bool:
        return self.is_clicked

    def getNeighbors(self) -> int:
        return self.neighbors

    def setNeighbors(self, value: int) -> None:
        self.neighbors = value

    def getRow(self) -> int:
        return self.row

    def getCol(self) -> int:
        return self.col

    def flagPiece(self) -> None:
        if self.flagged:
            self.flagged = False
        else:
            self.flagged = True

    def getFlagged(self) -> bool:
        return self.flagged