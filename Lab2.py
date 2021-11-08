#Created by: Lingling Wang, Xiaohan Zhao, Ruixin Li
#Group Tips on Format: 
#   Make sure use _ to seperate two words
#   Make sure you capitalized the first character of the variable name
#   Make sure you create a word for variable instead of a character only

import sys

board = {'1': ' ' , '2': ' ' , '3': ' ' ,
         '4': ' ' , '5': ' ' , '6': ' ' ,
         '7': ' ' , '8': ' ' , '9': ' ' }
#Identify the board key for the game

board_key = []

for enter_key in board:
    board_key.append(enter_key)
    #enter and append the key to the board

'''
function to create the board
'''
def full_board(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    #create the board for game

'''
function to setup player 1 and its input
'''
def Player1():
    print("Player 1's chance")
    player1_input = input("Enter the position between [1-9] where you want to mark:")
    #try except to do some expections on the user input
    try:
        empty_or_not(1,player1_input)
        player_key = 'X'

        if board[player1_input] == ' ':
            board[player1_input] = player_key
        
    except KeyError:
        if player1_input == 'quit' or player1_input == "Quit" or player1_input == "QUIT":
            print("Player 2 won, since player 1 quit the game!")
            sys.exit()
            #considered if player1 wants to end the game in the middle
        else:
            print('Please input value between [1-9]')
            Player1()
         
'''
function to setup player2 and its input
'''
def Player2():
    print("Player 2's chance")
    player2_input = input("Enter the position between [1-9] where you want to mark:")
    #try except to do some expections on the user input
    try:
        empty_or_not(2,player2_input)
        player_key = 'O'
        if board[player2_input] == ' ':
            board[player2_input] = player_key
                  
    except KeyError:
        if player2_input == 'quit' or player2_input == "Quit" or player2_input == "QUIT":
            print("Player 1 won, since player 1 quit the game!")
            sys.exit()
            #considered if player2 want to end the game in the middle.
        else:
            print('Please input value between [1-9]')
            Player2()

'''
set turns for different players
'''
def empty_or_not(player,n):
    sign = ''

    #Determine the sign for players
    if player == 1:
        sign = 'X'
    else:
        sign = 'O'

    
    if board[n] == ' ':
        board[n] == sign #Change the board if empty
    else:
        if player == 1: #Allow player input again
            print("Try again")
            Player1()
        else:
            print("Try again")
            Player2()
                  
'''
function to give players an option to play again
'''
def PlayAgain():
    play_again = input("Do want to play again? yes or no.").lower()
    #Consided the enter is not fully typed in lower case. Making sure the code is case sensitive.
    right_or_not = 0

    while  right_or_not == 0:
        if play_again in ['yes','no']: #Check if the input is right
            right_or_not += 1
        else:
            print("Please enter yes or no")
            play_again = input("Do want to play again? yes or no.").lower()

    if play_again == "yes":  #To see if the player wants to play again.
            for enter_key in board_key:
                board[enter_key] = " "
            game()

    elif play_again == "no":
        print("Thanks for playing! See you next time!")
        sys.exit()

'''
function to setup the game
'''
def game():
    print("Please Wait...")
    full_board(board)
    
    while True:
        key = 0
        for key in range(0,10):
            if key%2 == 0:
                #give player1 an identity as 1
                k = 1
                Player1()
                full_board(board)
            if key%2 == 1:
                #give player2 an identity as 2
                k = 2
                Player2()
                full_board(board)
            
            if board['1'] == board ['2'] == board ['3'] != ' ':
                print("Player",k,"won!")
                break
            if board['4'] == board ['5'] == board ['6'] != ' ':
                print("Player",k,"won!")
                break
            if board['7'] == board ['8'] == board ['9'] != ' ':
                print("Player",k,"won!")
                break
            #Above check if the any player won horizontally 
            if board['1'] == board ['4'] == board ['7'] != ' ':
                print("Player",k,"won!")
                break
            if board['2'] == board ['5'] == board ['8'] != ' ':
                print("Player",k,"won!")
                break
            if board['3'] == board ['6'] == board ['9'] != ' ':
                print("Player",k,"won!")
                break
            #Above check if the any player won vertically 
            if board['1'] == board ['5'] == board ['9'] != ' ':
                print("Player",k,"won!")
                break
            if board['3'] == board ['5'] == board ['7'] != ' ':
                print("Player",k,"won!")
                break
            #Above check if the any player won diagonally  
            if board['1'] != " " and board ['2'] != " " and board ['3'] != " " and board['4'] != " " and board ['5'] != " " and board ['6'] != " " and board['7'] != " " and board ['8'] != " " and board ['9'] != " ":
                print("No one won! This round is draw.")
                break
            #Above check if the the draw happens with all space filled

        PlayAgain()
                  
if __name__ == "__main__":
    game()
