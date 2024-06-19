import game
import board

game_size = (800, 800)
board = board.Board((20, 20), .2, game_size)
game = game.Game(board, game_size)
game.run()