import random

run = True

while run:
  guess = int(input("Guess the number:\n"))
  min, max = 1, 500
  num = random.randint(min, max)
  
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

    elif guess == max:
      guess = int(input("Max number\n"))

    else:
      guess = int(input("TOO HIGH\n"))
