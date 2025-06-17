computer_choice = 'rock'

user_choice = input('What path do you want to take rock, paper, or scissors?\n')

if computer_choice == user_choice:
     print('ITS A TIE!!')

elif user_choice == 'paper' and computer_choice == 'rock':
        print('YOU WIN!!')

elif user_choice == 'scissors' and computer_choice == 'rock':
        print('YOU LOSE, COMPUTER WINS!!')