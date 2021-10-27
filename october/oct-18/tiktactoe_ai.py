results_of_game = ['', '', '', '', 'O', '', 'X', '', ''] 
winners = ['012', '036', '048', '147', '258', '246', '345', '678']

def tiktactoe(results):
    check_for_winners = []
    for char in winners:
        check = ''
        for i in char:
            i = int(i)
            check = check + results[i]
        check_for_winners.append(check)

    if "XXX" in check_for_winners:
        return print("X wins!")
    elif "OOO" in check_for_winners:
        return print("O wins!")
    else:
        return print("Cat's Game!")

tiktactoe(results_of_game)

# from logic import get_winner

def get_move(board, letter):
   # STEP 1
   weights = [5, 1, 5, 1, 4, 1, 5, 1, 5]
   available_moves = get_available_moves(board)
   
   # STEP 2
   move_scores = [0] * 9
   for move_index in available_moves:
      move_scores[move_index] = get_score(board, letter, move_index)
   
   # STEP 3
   move_weighted_scores = []
   for i in range(9):
      move_weighted_scores.append(weights[i] * move_scores[i])
   
   # STEP 4
   return get_highest_index(move_weighted_scores)

def get_score(board, letter, move):
   temp_board = board[::]

   temp_board[move] = letter
   
   winner = tiktactoe(temp_board)

   if winner == '':
      return 1
   if winner == letter:
      return 50
   
   return -1

def get_highest_index(list_of_numbers):
   max_index = -1
   max_n = -1
   for i, n in enumerate(list_of_numbers):
      if n > max_n:
         max_index = i
         max_n = n

   return max_index

def get_available_moves(board):
   output = []
   for i in range(len(board)):
      if board[i] == '':
         output.append(i)
   
   return output

print(get_move(['X','X','O','O','X','O','O','',''], 'X'))
print(get_move(['X','X','O','O','O','O','','',''], 'O'))

#  3 | 1 | 3
# ---+---+---
#  1 | 5 | 1
# ---+---+---
#  3 | 1 | 3
# # STEP 1
# weights = [3, 1, 3, 1, 5, 1, 3, 1, 3]

#  0 | 1 | 1
# ---+---+---
#  0 | 0 | 1
# ---+---+---
#  1 | 1 | 0
# # STEP 2
# scores = [0, 1, 1, 0, 0, 1, 1, 1, 0]

#  0 | 1 | 3
# ---+---+---
#  0 | 0 | 1
# ---+---+---
#  3 | 1 | 0
# # STEP 3
# weighted_scores = [0, 1, 3, 0, 0, 1, 3, 1, 0]

# # STEP 4
# Pick the highest one, or one of the highest ones

# board = ['','','','','','','','','']
# board = ['X','X','O','O','X','O','O','','']
board = ['X','',''
        ,'O','','',
         'O','','']

user_input = input("Choose your mark, 'X' or 'O': ").upper()

if user_input == 'X':
    opponent_mark = 'O'
elif user_input == 'O':
    opponent_mark = 'X'
def get_winner(board):
   checks = [
      [0, 1, 2],
      [3, 4, 5],
      [6, 7, 8],
      [0, 3, 6],
      [1, 4, 7],
      [2, 5, 8],
      [0, 4, 8],
      [2, 4, 6]
   ]
   for indexes in checks:
      if board[indexes[0]] == board[indexes[1]] == board[indexes[2]] != '':
         return board[indexes[0]]
   
   return ''
   
def get_move(board, letter):
   # STEP 1
   weights = [5, 1, 5, 1, 6, 1, 5, 1, 5]
   available_moves = get_available_moves(board)
   
   # STEP 2
   move_scores = [0] * 9
   for move_index in available_moves:
      move_scores[move_index] = get_score(board, letter, move_index)
   
   # STEP 3
   move_weighted_scores = []
   for i in range(9):
      move_weighted_scores.append(weights[i] * move_scores[i])
   
   # STEP 4
   return get_highest_index(move_weighted_scores)

def get_score(board, letter, move):
   temp_board = board[::]

   temp_board[move] = letter
   
   winner = get_winner(temp_board)

   if winner == '':
      return 1
   if winner == letter:
      return 50
   
   return -1

def get_highest_index(list_of_numbers):
   max_index = -1
   max_n = -1
   for i, n in enumerate(list_of_numbers):
      if n > max_n:
         max_index = i
         max_n = n

   return max_index

def get_available_moves(board):
   output = []
   for i in range(len(board)):
      if board[i] == '':
         output.append(i)
   
   return output

def block_move(board):
    temp_board = board[::]
    # best_move_for_o = get_move(temp_board, 'O')

    # STEP 1
    weights = [5, 1, 5, 1, 4, 1, 5, 1, 5]
    available_moves = get_available_moves(temp_board)
   
    # STEP 2
    move_scores = [0] * 9
    for move_index in available_moves:
       move_scores[move_index] = get_score(temp_board, user_input, move_index)
   
   # STEP 3
    move_weighted_scores = []
    for i in range(9):
        temp_board.insert(get_move(board, opponent_mark), opponent_mark)
        if get_winner(temp_board) == user_input:
            move_weighted_scores.append(weights[i] * 50)
            temp_board = board[::]
        elif get_winner(temp_board) == opponent_mark:
            move_weighted_scores.append(weights[i] * 50)
            temp_board = board[::]
        else:
            move_weighted_scores.append(weights[i] * move_scores[i])
            temp_board = board[::]
    return get_highest_index(move_weighted_scores)
    # STEP 4
    # return get_highest_index(move_weighted_scores)


    # if is_o_a_winner == "O"
    # x goes in the best place for o
    # temp_board.insert(best_move_for_o, 'O')

    # if temp_board == 'X' == get_winner(temp_board):
    #     return 50
    # elif temp_board == 'O' == get_winner(temp_board):
    #     return 50
    # else:
    #     return get_highest_index(move_index)

#print(get_move(['X','X','O','O','X','O','O','',''], 'X'))
#print(get_move(['X','X','O','O','O','','','','O'], 'O'))
print(block_move(board))