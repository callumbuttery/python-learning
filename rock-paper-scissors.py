from enum import Enum

computer_choice = 'Paper'
user_choice = ''


Rock = 'Rock'
Paper = 'Paper'
Scissors = 'Scissors'

while user_choice.strip() =='' : 
    user_choice = input('Do you want Rock, Paper or Scissors? \n');


def checkForPlayerWin(choice):
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

checkForPlayerWin(user_choice)

