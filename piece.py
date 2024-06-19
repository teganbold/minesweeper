class Piece():
    def __init__(self, has_mine) -> None:
        self.has_mine = has_mine
        self.is_clicked = False
        self.neighbors = 0

    def hasMine(self):
        return self.has_mine

    def isClicked(self):
        return self.is_clicked

    def getNeighbors(self):
        return self.neighbors

    def click(self):
        self.is_clicked = True

