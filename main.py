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

rps = [rock, paper, scissors]

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors"))
if choice >= 3 or choice < 0:
  print("You type invalid number. You lose")
else:
  print(rps[choice])
  print("Computer choose:")
  x = len(rps)
  comp = random.randint(0, x - 1)
  print(rps[comp])

  if choice == 2 and comp == 1:
    print("You Win")
  elif choice == 0 and comp == 1:
    print("You Lose")
  elif choice == 0 and comp == 2:
    print("You Win")
  elif choice == 1 and comp == 0:
    print("You Win")
  elif choice == 1 and comp == 2:
    print("You Lose")
  elif choice == 2 and comp == 0:
    print("You Lose")
  else:
    print("Replay")