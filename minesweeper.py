# minesweeper.py - A simple minesweeper game

# We’ll be using the random and sys modules, so we import them
import random
import sys

'''The first thing we want to define is our layout for the board, which consists of rows and 
columns of numbers, with vertical and horizontal lines to divide them.
Our sole argument will be a list called nums, which will consist of numbers 1-9. 
'''
def layout(board):  
    '''We will print five lines, three of them representing our rows, and two representing the horizontal lines. 
    (TYPE THE ENTIRE FIRST LINE, COPY, & PASTE THREE TIMES)'''
    print(str(board[0]) + '|' + str(board[1]) + ' |' + str(board[2]))
    # ^ (Paste that three times, then print two more lines for the horizontal lines.) 
    print('-+--+-')
    print(str(board[3]) + '|' + str(board[4]) + ' |' + str(board[5]))
    print('-+--+-')
    print(str(board[6]) + '|' + str(board[7]) + ' |' + str(board[8]))
    # Then we change the numbers so that they’re all included. 
    '''Let’s test this real quick. Above layout, create a list called nums….and include numbers 1-9. 
    Now just run “layout(nums)”. This is what you should get. SWITCH BACK TO FILE'''

'''Delete “layout(nums)” and create game() func. Cut “nums” arr from global scale and paste in game(). 
The while true is the code we’ll be repeating every time the player takes a turn.'''
def game():
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    mine = random.choice(nums)
    print('\nCOLLECT ALL THE CASH AND AVOID STEPPING ON THE MINE')
    while True:
        # vvv gets number of ints in "nums" array. IGNORE TIL YOU GET TO "ELIF"
        numCount = len(list(filter(lambda x: (type(x) == int), nums))) 
        layout(nums)
        choice = int(input()) # 
        nums[choice - 1] = ' '
        print('🙂\n')
        
        if choice == mine:
            nums[choice - 1] = '💣'
            layout(nums)
            print('KABOOM. Game Over.')
            return

        elif numCount == 2:
            layout(list(map(lambda x: ' ' if x == choice - 1 else x, nums)))
            print('YOU HAVE SUCCESSFULLY CLEARED THE field.')
            return

while True:
    choice = input('\nready? y/n\n')
    if choice == 'y':
        game()
    elif choice == 'n':
        sys.exit()

# CODE READY TO ROLL
