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

#Write your code below this
game_images = [rock, paper, scissors]

your_choice = int(input("what do you choose ? type 0 for rock, 1 for paper or 2 for scissors.\n"))
if your_choice >= 3 or your_choice < 0 :
  print ("you typed a invalid number, you lose!")
  
else:
  print(game_images[your_choice])
  
  computer_choice = random.randint(0, 2)
  print("computer chose ")
  print(game_images[computer_choice])
  
  
  if your_choice == 0 and computer_choice == 2:
    print ("you win!")
  elif your_choice == 2 and computer_choice == 0:
    print ("you lose!")
  elif computer_choice > your_choice:
    print ("you lose!")
  elif your_choice > computer_choice:
    print ("you win!")
  elif your_choice == computer_choice:
    print("it's a Draw!")
    

