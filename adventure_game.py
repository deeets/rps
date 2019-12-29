#//simple rock, paper, scissors. Will add dialogue on the next go around.

'''imports'''
import time
import sys
import random

#//defines
def win():
    print('THE GAME: You Win!')

def lost():
    print('THE GAME: You Have Lost!')

def tie():
    print('THE GAME: Its A Tie!')

def the_game():
#//moves
    moves = ['rock', 'paper', 'scissors']

    print('THE GAME: Rock, Paper, Scissors?')
    attempts = 3

    while True:
        if attempts == 0:
            print('THE GAME: Incorrect Response, I told you this would happen! Bye!')
            time.sleep(3)
            the_game()

        player = str(input('Player: ')).lower()
        if player.lower() not in moves:
            print(f'THE GAME: That is not correct! You have {attempts} attempts left. Do not mess it up!')
            attempts -= 1
        else:
            computer = random.choice(moves)
            print(f'Computer: {computer}')

            if player == computer:
                tie()
            elif player == 'rock' and computer == 'scissors':
                win()
            elif player == 'rock' and computer == 'paper':
                lost()
            elif player == 'paper' and computer == 'rock':
                win()
            elif player == 'paper' and computer == 'scissors':
                lost()
            elif player == 'scissors' and computer == 'paper':
                win()
            elif player == 'scissors' and computer == 'rock':
                lost()
            else:
                pass

            play_again = str(input('THE GAME: Try Again? (y/n): '))
            if play_again.lower() == 'y':
                the_game()
            elif play_again.lower() == 'n':
                print('THE GAME: Game Over. Bye!')
                time.sleep(2.5)
                the_game()
            else:
                print('THE GAME: Incorrect Results. Bye!')
                time.sleep(2.5)
                the_game()


if __name__=='__main__':
    the_game()