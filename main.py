import random

num = random.randint(1, 1000000000000000000)

guess = int(input("Guess the number!!!\n"))

guessed = False

while guessed == False:
  if guess > num:
    int(input("Greater.\n"))
    
  elif guess < num:
    int(input("Less.\n"))
    
  else:
    print("You win!!!")
