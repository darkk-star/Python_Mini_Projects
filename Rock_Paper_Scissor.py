import random

user_wins = 0
cpu_wins = 0

options = ["rock","paper","scissors"]

while(True):
    user_input = input("Type Rock/Paper/Scissors or q to quit: ").lower()

    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0,2)
    cpu_choice = options[random_number]

    print("CPU picked",cpu_choice)

    if(user_input == "rock" and cpu_choice == "scissors"):
        print("You won!")
        user_wins+=1
    
    elif(user_input == "paper" and cpu_choice == "rock"):
        print("You won!")
        user_wins+=1
    
    elif(user_input == "scissors" and cpu_choice == "paper"):
        print("You won!")
        user_wins+=1

    else:
        print("You lost!")
        cpu_wins+=1

print("\n\nGame Over!")
print("User won",user_wins,"times!")
print("CPU won",cpu_wins,"times!")

    

    

