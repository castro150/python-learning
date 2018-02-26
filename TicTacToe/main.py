from __future__ import print_function
from IPython.display import clear_output


VALID_POSITION_INPUT = ('0', '1', '2', '3', '4', '5', '6', '7', '8')


def display_board(board):
    clear_output()
    board_string = '''
    \n\n {} | {} | {} \n --------- \n {} | {} | {} \n --------- \n {} | {} | {} \n\n
    '''.format(board[0], board[1], board[2], board[3], board[4], board[5], board[6], board[7], board[8])
    print(board_string)


def player_input():
    value = raw_input('Type the position you want to mark: ')
    while value not in VALID_POSITION_INPUT:
        value = raw_input('Invalid value! Type a valid position: ')
    return value


def place_marker(board, marker, position):
    board[position] = marker


def next_marker(marker):
    if marker == 'X':
        return 'O'
    return 'X'


def win_check(board, mark):
    if board[0] == board[1] == board[2] == mark:
        print('Player {} won!'.format(mark))
        return True
    elif board[3] == board[4] == board[5] == mark:
        print('Player {} won!'.format(mark))
        return True
    elif board[6] == board[7] == board[8] == mark:
        print('Player {} won!'.format(mark))
        return True
    elif board[0] == board[3] == board[6] == mark:
        print('Player {} won!'.format(mark))
        return True
    elif board[1] == board[4] == board[7] == mark:
        print('Player {} won!'.format(mark))
        return True
    elif board[2] == board[5] == board[8] == mark:
        print('Player {} won!'.format(mark))
        return True
    elif board[0] == board[4] == board[8] == mark:
        print('Player {} won!'.format(mark))
        return True
    elif board[2] == board[4] == board[6] == mark:
        print('Player {} won!'.format(mark))
        return True
    return False


def space_check(board, position):
    return board[position] in VALID_POSITION_INPUT


def full_board_check(board):
    for position in board:
        if position in VALID_POSITION_INPUT:
            return False
    print('Board is full!')
    return True


def player_choice(board):
    position = int(player_input())
    while not space_check(board, position):
        print('This position is not free!')
        position = int(player_input())
    return position


def replay():
    answer = raw_input('Do you want to play again? (y/n) ')
    return answer.lower() == 'y'


def play():
    board = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
    actual_marker = 'X'

    while not full_board_check(board) and not win_check(board, 'X') and not win_check(board, 'O'):
        display_board(board)
        position = player_choice(board)
        place_marker(board, actual_marker, position)
        actual_marker = next_marker(actual_marker)
    else:
        if replay():
            play()

play()
