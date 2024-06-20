from game import Game
from board import Board

game_size = (800, 800)
board = Board((20, 20), .15, game_size)
game = Game(board, game_size)
game.run()