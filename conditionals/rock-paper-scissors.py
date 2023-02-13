from enum import Enum
import random


Rock = 'Rock'
Paper = 'Paper'
Scissors = 'Scissors'

moveArray = [Rock, Paper, Scissors]

def checkForPlayerWin(choice, computer_choice):
    print(choice == computer_choice)
    print('computer choice: ', computer_choice)
    if choice.capitalize() == computer_choice :
        print('Game tied')
    elif choice.capitalize() == Rock and computer_choice == Scissors :
        print('Player wins')
    elif choice.capitalize() == Scissors and computer_choice == Paper :
        print ('Player wins')
    elif choice.capitalize() == Paper and computer_choice == Rock :
        print('Player wins')
    else :
        print('Computer wins')

def runGame() :
    computer_choice = random.choice(moveArray).capitalize()

    user_choice = ''

    while user_choice.strip() =='' : 
        user_choice = input('Do you want Rock, Paper or Scissors? \n');

    checkForPlayerWin(user_choice, computer_choice)


runGame()

