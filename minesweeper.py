#! python3
# minesweeper.py - A simple minesweeper game

import random
import sys

# Hashtag board
def layout(board):  
    print(str(board[0]) + '|' + str(board[1]) + ' |' + str(board[2]))
    print('-+--+-')
    print(str(board[3]) + '|' + str(board[4]) + ' |' + str(board[5]))
    print('-+--+-')
    print(str(board[6]) + '|' + str(board[7]) + ' |' + str(board[8]))

# Game Logic
def game():
    field = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    #mine = random.choice(field)
    mine = field[8]
    print('\nCOLLECT ALL THE CASH AND AVOID STEPPING ON THE MINE')
    while True:
        numCount = len(list(filter(lambda x: (type(x) == int), field))) 
        layout(field)
        choice = int(input())
        field[choice - 1] = ' '
        print('🙂\n')
        
        if choice == mine:
            field[choice - 1] = '💣'
            layout(field)
            print('KABOOM. Game Over.')
            return

        elif numCount == 2:
            layout(list(map(lambda x: ' ' if x == choice - 1 else x, field)))
            print('YOU HAVE SUCCESSFULLY CLEARED THE FIELD.')
            return

# play again loop
while True:
    choice = input('\nready? y/n\n')
    if choice == 'y':
        game()
    elif choice == 'n':
        sys.exit()

# CODE READY TO ROLL
