from enum import Enum
import random


Rock = 'Rock'
Paper = 'Paper'
Scissors = 'Scissors'
game_counter = 1

computer = 0
person = 0
draw = 0



print('Best of 3 - Rock, Paper, Scissors')

moveArray = [Rock, Paper, Scissors]

def incrementGames(winner):
    global person, computer, draw, game_counter
    print(winner + ' won that round')
    if winner == 'player':
        person += 1
    elif winner == 'computer' :
        computer += 1
    else :
        draw += 1

    print('Score: \n' + 'Computer: ' + str(computer) + '\n' + 'Person: ' + str(person) + '\n' + 'Ties: ' + str(draw) + '\n\n')  

    if game_counter < 3:
        game_counter += 1
        runGame()
    else :
        print('Results: \n' + 'Computer wins: ' + str(computer) + '\n' + 'Person wins: ' + str(person) + '\n' + 'Ties: ' + str(draw) + '\n\n')
        if computer < person :
            print('Player is the winner!')
        elif person < computer:
            print('Computer is the winner!')
        else :
            print('Tie!')


def checkForPlayerWin(choice, computer_choice):
    print('computer choice: ', computer_choice)
    if choice.capitalize() == computer_choice :
        incrementGames('tie')
    elif choice.capitalize() == Rock and computer_choice == Scissors :
        incrementGames('player')
    elif choice.capitalize() == Scissors and computer_choice == Paper :
        incrementGames('player')
    elif choice.capitalize() == Paper and computer_choice == Rock :
        incrementGames('player')
    else :
        incrementGames('computer')

def runGame() :
    computer_choice = random.choice(moveArray).capitalize()

    user_choice = ''

    print('Game ' + str(game_counter) +'\n\n')
    while user_choice.strip() =='' : 
        user_choice = input('Do you want Rock, Paper or Scissors? \n');

    checkForPlayerWin(user_choice, computer_choice)

runGame()

