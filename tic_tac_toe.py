def display_board(board):
  print('\n' * 100)
  print("Here is the current board: ")
  print(board[7] + '|' + board[8] + '|' + board[9])
  print(board[4] + '|' + board[5] + '|' + board[6])
  print(board[1] + '|' + board[2] + '|' + board[3])


def player_input():
  marker = ""

  while marker != 'X' and marker != 'O':
    marker = input('Player1: Choose X or O:').upper()

  if marker == 'X':
    return ('X', 'O')
  else:
    return ('O', 'X')


palyer1_marker, player2_marker = player_input()

print(palyer1_marker)
