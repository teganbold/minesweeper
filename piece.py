class Piece():
    def __init__(self, has_mine, row, col) -> None:
        self.has_mine = has_mine
        self.is_clicked = False
        self.row = row
        self.col = col
        self.neighbors = 0

    def hasMine(self):
        return self.has_mine

    def isClicked(self):
        return self.is_clicked

    def getNeighbors(self):
        return self.neighbors

    def getRow(self):
        return self.row

    def getCol(self):
        return self.col

    def click(self):
        self.is_clicked = True

    def setNeighbors(self, value):
        self.neighbors = value


