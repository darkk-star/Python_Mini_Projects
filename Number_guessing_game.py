#importing random module
import random

#user giving upper range
upper_limit = int(input("Type a number: "))

if upper_limit <= 0:
    print("Enter number greter than 0")
    quit()

count=0

#generating random number
random_number =random.randrange(0,upper_limit)

while(True):
    count += 1
    guess = int(input("Guess the number: "))

    if(guess == random_number):
        print("You guessed correct number in ",count,"try!")
        break
    else:
        if(guess > random_number):
            print("You guessed greater number")
        else:
            print("You guessed lesser number")

