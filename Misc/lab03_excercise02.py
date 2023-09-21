#Author: Jonathan Bankston
#KUID: 3097029
#Date: 2/16/23
#Lab: lab03
#Last modified: 2/17/23
#Purpose: This program prompts the user to guess a hidden word with hints along the way

word = "bringcoffee"

print("Guess the hidden phrase!")

count = 0
while True:
  guess = input("Guess: ")
  guess = guess.lower()
  count = count + 1
  if len(guess) < 11:
    print("Not enough characters")
  elif len(guess) > 11:
    print("Too many characters")
  else:
    if guess == word:
      print("You guessed correctly")
      break
    icount = 0
    for i in range(11):
      if guess[i] == word[i]:
        icount = icount + 1
      else:
        break
    print(f"Correct letters: {icount}")

print(f"Number of guesses: {count}")


