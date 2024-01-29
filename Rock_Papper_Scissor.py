

Rock = print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')

Paper = print('''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
''')

Scissors = print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')

Game = [Rock , Paper , Scissors]
import random


user_choice = int(input("What do you choose ? Type 0 for Rock , 1 for paper , 2 for scissors:\n"))
print(Game[user_choice])

comp_choice = random.randint(0, 2)
print("Computer Choice:")
print(Game[comp_choice])

if user_choice == 0 and comp_choice == 2:
    print("You Win!")
elif user_choice == 2 and comp_choice == 0:
    print("You lose!")
elif comp_choice > user_choice:
    print("You lose!")
elif comp_choice == user_choice:
    print("It's a draw.")
elif comp_choice < user_choice:
    print("You Win!")
elif user_choice >= 3 or user_choice < 0:
    print("Invalid Input, YOU LOSE :(")
