# Created by: DMInnovations

import random

run = True

while run:
  guess = int(input("Guess the number:\n"))
  num = random.randint(1, 500)

  guessing = True

  while guessing:
    if guess == num:
      print("You win!")
      guessing = False

    elif guess < int(num - 20):
      guess = int(input("Colder\n"))

    elif guess > int(num + 20):
      guess = int(input("Warmer\n"))

    elif guess > int(num - 20) or guess < int(num + 20):
      guess = int(input("Hot!\n"))

    else:
      guess = int(input("Keep trying\n"))
