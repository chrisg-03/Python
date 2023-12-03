'''
1. Create a tic tac toe board 
2. Choose position 1-9, replace square with player icon
3. Check if winnming condition or tie; add condition that tie can only exist if board is full
4. Switch player repeat steps 2 and 3
5. Bring it all together into a game
'''

# Create a tic tac toe board
board = [1,2,3,4,5,6,7,8,9]
winner = None
player = 'x'

# Draw board
def get_board(board):
    for i in range(0, len(board), 3):
        print('|'.join(map(str, board[i: i + 3])))

# Player chooses position
def get_position(board, player):
    z = int(input('Choose your square'))
    if (1 <= z <= 9) and (isinstance(board[z - 1], int)):
        board[z - 1] = player
        return True
    else:
        print('Invalid move. Try again')
        return False

# Check for win conditions
def check_win(board):
    global winner
    if board[0] == board[1] == board[2]:
        winner = player
        return True
    elif board[3] == board[4] == board[5]:
        winner = player
        return True
    elif board[6] == board[7] == board[8]:
        winner = player
        return True
    elif board[0] == board[4] == board[8]:
        winner = player
        return True
    elif board[2] == board[4] == board[6]:
        winner = player
        return True
    return False

# Check for tie
def check_tie(board):
    return all(isinstance(cell, str) for cell in board)

# Switch players at the end of each turn
def switch_player(player):
    return 'o' if player == 'x' else 'x'

# Tic Tac Toe is created!
print("Let's play a game of tic tac toe, choose a number from 1 - 9\n")
while winner is None:
    while not get_position(board, player):
        print('\n---\n')
        pass
    if check_win(board):
        get_board(board)
        print(f'\n{winner} wins!')
        break
    elif check_tie(board):
        get_board(board)
        print("\nLet's call it even")
    player = switch_player(player)
    get_board(board)
    print('\n---\n')