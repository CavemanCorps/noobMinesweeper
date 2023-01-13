#! python3
# minesweeper.py - A small minesweeper-esque game

import random
import sys

# Hashtag board

# board is simply an arr of nums to map here
'''
def layout(board):  
    print(str(board[1]) + '|' + str(board[2]) + ' |' + str(board[3]))
    print('-+--+-')
    print(str(board[4]) + '|' + str(board[5]) + ' |' + str(board[6]))
    print('-+--+-')
    print(str(board[7]) + '|' + str(board[8]) + ' |' + str(board[9]))
'''

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
    mine = field[8] # 9
    print('\nCOLLECT ALL THE CASH AND AVOID STEPPING ON THE MINE')
    while True:
        
        numCount = len(list(filter(lambda x: (type(x) == int), field))) 
        print("NUMBER OF NUMS: ", numCount)

        layout(field)
        choice = int(input())
        field[choice - 1] = ' '
        print('🙂')

        #if choice != mine:

        
        if choice == mine:
            field[choice - 1] = '💣'
            print('KABOOM. Game Over.')
            return

        elif numCount == 2:
            field[choice - 1] = ' '
            layout(field)
            print('YOU HAVE SUCCESSFULLY CLEARED THE FIELD.')
            return           
    return
    
while True:
    choice = input('\nready? y/n\n')
    if choice == 'y':
        game()
    elif choice == 'n':
        sys.exit()

# BREAKING OUT OF A FUNC: "return"
# https://www.quora.com/How-do-I-get-out-of-a-function-in-Python-using-break
# YOU KNOW WHAT: might just be better if I use a while loop instead.






















