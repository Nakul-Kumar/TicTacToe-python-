from IPython.display import clear_output

def display_board(board):
    clear_output()
    print('\t'+'   |   ' + '   |   ')
    print('\t'+board[1] + '  |  ' + board[2] + '   |   ' + board[3])
    print('\t'+'   |   ' + '   |   ')
    print('     ----------------------')
    print('\t'+'   |   ' + '   |   ')
    print('\t'+board[4] + '  |  ' + board[5] + '   |   ' + board[6])
    print('\t'+'   |   ' + '   |   ')
    print('     ----------------------')
    print('\t'+'   |   ' + '   |   ')
    print('\t'+board[7] + '  |  ' + board[8] + '   |   ' + board[9])
    print('\t'+'   |   ' + '   |   \n')
    pass

def player_input():
    player1 = ' '
    player2 = ' '
    while player1 not in ['X','O']:
        player1 = input('Player 1: Which side would you like to take X or O? ').upper()
        if player1 not in ['X','O']:
            print('Sorry invalid option please choose a valid option.\n')
    if player1 == 'X':
        return ('X','O')
    else:
        return ('O','X')

def place_marker(board, marker, position):
    board[position] = marker
    pass

def win_check(board, mark):
    return board[1]==mark and board[2]==mark and board[3]==mark or board[4]==mark and board[5]==mark and board[6]==mark or board[7]==mark and board[8]==mark and board[9]==mark or board[1]==mark and board[4]==mark and board[7]==mark or board[2]==mark and board[5]==mark and board[8]==mark or board[3]==mark and board[6]==mark and board[9]==mark or board[1]==mark and board[5]==mark and board[9]==mark or board[3]==mark and board[5]==mark and board[7]==mark
    pass

import random

def choose_first():
    if random.randint(0,1) == 0:
        return('Player 2')
    else:
        return('Player 1')

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    for num in range(1,10):
        if space_check(board,num):
            return False
    return True

def player_choice(board):
    position = 0
    while position not in ['1','2','3','4','5','6','7','8','9'] or not space_check(board,position):
        position = (input('Please enter a number from 1-9 so the symbol can be placed: '))
        if position not in ['1','2','3','4','5','6','7','8','9']:
            print('\nInvalid Number!! Please try again\n')
            position = 0
        else:
            position = int(position)
            break
    return position
    pass

def replay():
    return input('Would you like to play again? (Y or N): ').lower().startswith('y')
    pass

print('Welcome to Tic Tac Toe!\n')

while True:
    theBoard = [' ']*10

    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn, ' will go first!\n')

    play_game = input('Are you both ready to play the game! :  ')

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':

            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker,position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! Player 1 You have won the game!!\n')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!\n')
                    game_on = False
                else:
                    turn = 'Player 2'

        else:
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker,position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Congratulations! Player 2 you have won the game!!\n')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!\n')
                    game_on = False
                else:
                    turn = 'Player 1'

    if not replay():
        print('\nThank you for playing, Do play again!!\n')
        break
