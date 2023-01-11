#! python3
# minesweeper.py - A small minesweeper-esque game

import random
import sys

# Hashtag board

# board is simply an arr of nums to map here
def layout(board):  
    print(str(board[0]) + '|' + str(board[1]) + ' |' + str(board[2]))
    print('-+--+-')
    print(str(board[3]) + '|' + str(board[4]) + ' |' + str(board[5]))
    print('-+--+-')
    print(str(board[6]) + '|' + str(board[7]) + ' |' + str(board[8]))


# Game Logic

def game():
    field = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    mine = random.choice(field)
    
    print('\nCOLLECT ALL THE CASH AND AVOID STEPPING ON THE MINE')
    for i in range(0, 8):   # THIS IS EXCLUSIVE OF LAST NUMBER
        fieldNum = len(list(filter(lambda x: (type(x) == int), field))) - 1
        print('\nTURNS REMAINING:', fieldNum)
        layout(field)
        choice = int(input())
        field[choice - 1] = ' '

        print(mine)
        if choice == mine or i == 8:
            field[choice - 1] = 'X'
            layout(field)
            print('KABOOM. Game Over.')
            #game()
            return
    
    print('YOU HAVE SUCCESSFULLY CLEARED THE FIELD.')
    #game()
    return
    
while True:
    choice = input('ready? y/n\n')
    if choice == 'y':
        game()
    if choice == 'n':
        sys.exit()

# TODO: RELOOP THIS SHIT BY ASKING "PLAY AGAIN?"
# BREAKING OUT OF A FUNC: "return"
# https://www.quora.com/How-do-I-get-out-of-a-function-in-Python-using-break























