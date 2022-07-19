""" This project will create a number guessing game in the form of virtual dice.  Enjoy!"""

# imports the randint function from the random module
from random import randint
# imports the sleep function from the time module
from time import sleep

# Function takes no arguments
def get_user_guess():
  guess = int(input("Guess a number: "))
  return guess

# Second funtion roll dice
def roll_dice(number_of_sides):
  first_roll = randint(1, number_of_sides)
  second_roll = randint(1, number_of_sides)
#maximum value the program can roll
  max_val = number_of_sides * 2 
  print ("The maximum possible value is: %d" % (max_val))
  guess = get_user_guess()
# verifying the user does not guess an invalid roll
  if guess > max_val:
    print ("You cannot guess a number higher then the possible value!")
# sleep function simulates rolling for two seconds
  else:
    print ("Rolling... ")
    sleep(2)
    print ("Your first roll is %d" % first_roll)
    sleep(1)
    print ("Your second roll is %d" % second_roll)
# Equates the total roll of both rolls
    total_roll = first_roll + second_roll
    print ("Your total roll is %d" % total_roll)
    print ("Result...")
    sleep(1)
    if guess == total_roll:
      print ("You have won the game!")
    else:
      print ("You have lost the game")
# Sides of Die
roll_dice(6)