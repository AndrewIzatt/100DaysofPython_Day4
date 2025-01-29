import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
options =[rock, paper, scissors]
play = "Y"
while play == "Y":
    you = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))
    computer = random.randint(0, 2)
    print(options[you])
    print("Computer chose:\n")
    print(options[computer])

    if you == computer:
        print("Tie.\n")
    elif (you - computer == -1) or (you - computer == 2):
        print("Computer wins.\n")
    else:
        print("You win.\n")

    play = input("Do you want to play again? Y or N\n")
