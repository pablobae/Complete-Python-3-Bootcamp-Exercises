import re

PLAYER_1 = 'player1'
PLAYER_2 = 'player2'
MAX_MOVEMENTS = 9
MARK_X = 'X'
MARK_O = 'O'


def game_on():
    print('Welcome to Tic Tac Toe!')

    board = {'7': ' ', '8': ' ', '9': ' ',
             '4': ' ', '5': ' ', '6': ' ',
             '1': ' ', '2': ' ', '3': ' '}

    user_marks = request_players_marks()
    wait_players_ready()
    display_board(board)

    game_finished = False
    current_player = PLAYER_1
    movement_counter = 0

    while not game_finished:
        request_move(board, current_player, user_marks[current_player])
        movement_counter += 1
        display_board(board)
        if check_winner(board, user_marks[current_player]):
            print('*** ' + current_player + ' has won!!')
            game_finished = True
        elif movement_counter == MAX_MOVEMENTS:
            print('TIE. There are no more available movements')
            game_finished = True
        else:
            current_player = swap_player(current_player)


def request_players_marks():
    players_marks = {}
    player1_mark = ''
    while player1_mark == '':
        answer = input(PLAYER_1 + ': Do you want to be ' + MARK_X + ' or ' + MARK_O + '? ')
        answer = answer.upper()
        if answer == MARK_X:
            player1_mark = answer
            players_marks[PLAYER_1] = player1_mark
            players_marks[PLAYER_2] = MARK_O
        elif answer == MARK_O:
            player1_mark = answer
            players_marks[PLAYER_1] = player1_mark
            players_marks[PLAYER_2] = MARK_X

    print(PLAYER_1 + ' will go first.')

    return players_marks


def wait_players_ready():
    ready = False
    while not ready:
        answer = input('Are you ready to play? Enter Yes or No: ')
        answer = answer.lower()
        if answer == 'yes':
            ready = True


def request_move(board, player, user_mark):
    is_valid_position = False
    while not is_valid_position:
        position = input(player + ', choose your next position (1-9): ')
        if not re.match('^[1-9]$', position):
            print('Position not valid: enter a number from 1 to 9')
        elif not board[position] == ' ':
            print('Position not valid: that position was already played')
        else:
            board[position] = user_mark
            is_valid_position = True


def display_board(board):
    print(f" {board['7']} | {board['8']} | {board['9']}")
    print('-----------')
    print(f" {board['4']} | {board['5']} | {board['6']}")
    print('-----------')
    print(f" {board['1']} | {board['2']} | {board['3']}")


def swap_player(player):
    if player == PLAYER_1:
        return PLAYER_2
    else:
        return PLAYER_1


def check_winner(board, mark):
    winning_combinations = [
        ['7', '8', '9'],
        ['4', '5', '6'],
        ['1', '2', '3'],
        ['1', '4', '7'],
        ['2', '5', '8'],
        ['3', '6', '9'],
        ['3', '5', '7'],
        ['1', '5', '9']
    ]

    for combination in winning_combinations:
        is_winner = True
        for item in combination:
            if not board[item] == mark:
                is_winner = False
                break
        if is_winner:
            break

    return is_winner


# Go!
game_on()
