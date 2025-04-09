from tictactoe import player, EMPTY, X, O, actions, result, winner, terminal, max_value, min_value, minimax

board = [[O, X, X],
        [X, O, X],
        [O, EMPTY, EMPTY]]
print(min_value(board))
print(minimax(board))
print(max_value(board))