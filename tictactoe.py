# write your code here
print('Enter cells: ')
game_state = input()
print('---------')
print(f'| {game_state[0]} {game_state[1]} {game_state[2]} |')
print(f'| {game_state[3]} {game_state[4]} {game_state[5]} |')
print(f'| {game_state[6]} {game_state[7]} {game_state[8]} |')
print('---------')

# cases of X winning
X_win_1 = game_state[0] == game_state[1] == game_state[2] == 'X'
X_win_2 = game_state[3] == game_state[4] == game_state[5] == 'X'
X_win_3 = game_state[6] == game_state[7] == game_state[8] == 'X'
X_win_4 = game_state[0] == game_state[3] == game_state[6] == 'X'
X_win_5 = game_state[1] == game_state[4] == game_state[7] == 'X'
X_win_6 = game_state[2] == game_state[5] == game_state[8] == 'X'
X_win_7 = game_state[0] == game_state[4] == game_state[8] == 'X'
X_win_8 = game_state[6] == game_state[4] == game_state[2] == 'X'

# cases of O winning
O_win_1 = game_state[0] == game_state[1] == game_state[2] == 'O'
O_win_2 = game_state[3] == game_state[4] == game_state[5] == 'O'
O_win_3 = game_state[6] == game_state[7] == game_state[8] == 'O'
O_win_4 = game_state[0] == game_state[3] == game_state[6] == 'O'
O_win_5 = game_state[1] == game_state[4] == game_state[7] == 'O'
O_win_6 = game_state[2] == game_state[5] == game_state[8] == 'O'
O_win_7 = game_state[0] == game_state[4] == game_state[8] == 'O'
O_win_8 = game_state[6] == game_state[4] == game_state[2] == 'O'

# cases of draw
draw = game_state[0] != '_' and game_state[1] != '_' and game_state[2] != '_' \
        and game_state[3] != '_' and game_state[4] != '_' and game_state[5] != '_' \
        and game_state[6] != '_' and game_state[7] != '_' and game_state[8] != '_'

# cases of Impossible
impossible_1 = (X_win_1 or X_win_2 or X_win_3 or X_win_4 \
                or X_win_5 or X_win_6 or X_win_7 or X_win_8) \
                and \
               (O_win_1 or O_win_2 or O_win_3 or O_win_4 \
                or O_win_5 or O_win_6 or O_win_7 or O_win_8)
## prep for impossbible_2: count number of X and O
count_X = 0
count_O = 0
for state in game_state:
    if state == 'X':
        count_X += 1
    elif state == 'O':
        count_O += 1
difference = count_X - count_O
if difference < 0:
    difference *= (-1)

impossible_2 = difference >= 2

if impossible_1 or impossible_2:
    print("Impossible")
elif X_win_1 or X_win_2 or X_win_3 or X_win_4 or X_win_5 or X_win_6 or X_win_7 or X_win_8:
    print("X wins")
elif O_win_1 or O_win_2 or O_win_3 or O_win_4 or O_win_5 or O_win_6 or O_win_7 or O_win_8:
    print("O wins")
elif draw:
    print("Draw")
else:
    print("Game not finished")