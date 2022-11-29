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

#Write your code below this line 👇
y = (input("Rock, Paper, Scissors : ")).lower()
if y == "rock" :
  print(rock)
elif y == "paper" :
  print(paper)
elif y == "scissors": 
  print(scissors)
x = random.randint(0,2)
if x == 0 :
  print(rock)
elif x == 1 :
  print(paper)
elif x == 2: 
  print(scissors)

if (x == 0 and y == "rock") or (x == 1 and y == "paper") or (x == 2 and y == "scissors")  :
  print("Tie")
elif (x == 0 and y == "paper") or (x == 1 and y == "scissors") or (x == 2 and y == "rock")  :
  print("You Won")
elif (x == 0 and y == "scissors") or (x == 1 and y == "rock") or (x == 2 and y == "paper")  :
  print("You Lost")