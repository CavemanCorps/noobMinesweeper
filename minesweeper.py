#! python3
# minesweeper.py - A small minesweeper-esque game
import random
import sys


# Hashtag board
field = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def layout(board):
    print(str(field[0]) + '|' + str(field[1]) + ' |' + str(field[2]))
    print('-+--+-')
    print(str(field[3]) + '|' + str(field[4]) + ' |' + str(field[5]))
    print('-+--+-')
    print(str(field[6]) + '|' + str(field[7]) + ' |' + str(field[8]))

# Game Logic
while True:
    print('COLLECT ALL THE CASH AND AVOID STEPPING ON THE MINE')
    nul = '$'
    boom = 'X'
    for i in range(1, 9):
        layout(field)
        mine = random.choice(field)
        choice = int(input())
        field[choice - 1] = nul

        if choice == mine:
            field[choice - 1] = boom
            layout(field)
            print('KABOOM')
            sys.exit()
    print('YOU HAVE SUCCESSFULLY CLEARED THE FIELD')
