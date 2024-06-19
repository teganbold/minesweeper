import game
import board

game_size = (800, 800)
board = board.Board((9, 9))
game = game.Game(board, game_size)
game.run()