#! python3
# minesweeper.py - A small minesweeper-esque game

import random
import sys

# Hashtag board

# board is simply an arr of nums to map here
def layout(board):  
    print(str(board[1]) + '|' + str(board[2]) + ' |' + str(board[3]))
    print('-+--+-')
    print(str(board[4]) + '|' + str(board[5]) + ' |' + str(board[6]))
    print('-+--+-')
    print(str(board[7]) + '|' + str(board[8]) + ' |' + str(board[9]))


# Game Logic

def game():
    field = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    #mine = random.choice(field)
    mine = field[9] # 9
    maxTurns = maxTurnsCopy = 9
    
    print('\nCOLLECT ALL THE CASH AND AVOID STEPPING ON THE MINE')
    # for i in range(0, maxTurns):   # THIS IS EXCLUSIVE OF LAST NUMBER
    for i in range(1, 9):
        # print('\nTURNS REMAINING:', maxTurnsCopy)
        print('\nTURNS:', i)
        layout(field)
        choice = int(input())
        # field[choice - 1] = ' '
        field[choice] = ' '
        maxTurnsCopy -= 1
        print(i)
        
        # if choice == mine or maxTurnsCopy == 8:
        if choice == mine or i == 8:
            #field[choice - 1] = '💣'
            field[choice] = '💣'
            layout(field)
            print('KABOOM. Game Over.')
            return
        else:
            print('\n🙂')
                
    print('YOU HAVE SUCCESSFULLY CLEARED THE FIELD.')
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






















