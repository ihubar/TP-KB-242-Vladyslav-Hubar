from random import choice

def user_choise_stone():
  if random_choise == "scissor":
    print("You win!!!")
  elif random_choise == "stone":
    print("Draw!!!")
  else:
    print("You lose!!!")

def user_choise_scissor():
  if random_choise == "paper":
    print("You win!!!")
  elif random_choise == "scissor":
    print("Draw!!!")
  else:
    print("You lose!!!")

def user_choise_paper():
  if random_choise == "stone":
    print("You win!!!")
  elif random_choise == "paper":
    print("Draw!!!")
  else:
    print("You lose!!!")


while True:
  user_choise = input("Please enter on of the 'stone', 'scissor', 'paper': ")
  print("Your choice: ", user_choise)

  random_choise = choice(["stone", "scissor", "paper"])
  print("Computer choise: ", random_choise)

  if user_choise == "stone":
    user_choise_stone()
  elif user_choise == "scissor":
    user_choise_scissor()
  elif user_choise == "paper":
    user_choise_paper()
  else:
    print("Please enter correct choice")