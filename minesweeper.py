# minesweeper.py -a simple minsweeper-based game

import random
import sys


def layout(board):
    print(str(board[0]) + '|' + str(board[1]) + ' |' + str(board[2]))
    print('-+--+-')
    print(str(board[3]) + '|' + str(board[4]) + ' |' + str(board[5]))
    print('-+--+-')
    print(str(board[6]) + '|' + str(board[7]) + ' |' + str(board[8]))

def game():
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    mine = random.choice(nums)
    print('\nMINESWEEPER BY ROMAN NAVARRO')
    while True:
        numCount = None
        layout(nums)
        choice = int(input())
        nums[choice - 1] = ' '
        print('🙂\n')

        if choice == mine:
            nums[choice - 1] = '💣'
            layout(nums)
            print('KABOOM. Game Over.')
            return

        elif numCount == 2:
            layout(list(map(lambda x: ' ' if x == choice - 1 else x, nums)))
            print('YOU HAVE SUCCESSFULLY CLEARED THE FIELD.')
            return

while True:
    choice = input('\nready? y/n\n')
    if choice == 'y':
        game()
    elif choice == 'n':
        sys.exit()
