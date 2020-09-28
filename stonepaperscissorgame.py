#Rock Paper Scissor Game
import random

print("Welcome To Rock Paper Scissor Game")

val = ['R','P','S']
chance = 0
r_point = 0
y_point = 0

print("How Many Chance You Want:")
t_chance = int(input())

print("R for Rock, P for Paper, S for Scissor")

while chance < t_chance:

    choice = input().upper()
    rand = random.choice(val)

    if choice == rand:
        print("It's Tie Point = 0")

    elif choice == "R" and rand == "S":
        y_point = y_point + 1
        print("You Won")

    elif choice == "S" and rand == "R":
         r_point = r_point + 1
         print("You Loose")

    elif choice == "S" and rand == "P":
         y_point = y_point + 1
         print("You Won")

    elif choice == "P" and rand == "S":
         r_point = r_point + 1
         print("You Loose")

    elif choice == "P" and rand == "R":
          y_point = y_point + 1
          print("You Won")

    elif choice == "R" and rand == "P":
        r_point = r_point + 1
        print("You Loose")

    else:
        print("Wrong Input")

    chance = chance + 1
    print(f"{t_chance - chance} is left out of {t_chance} \n")

if rand > choice:
    print(f"'Sorry!' You Losse The Game, Your Point is: {y_point}" )
elif rand == choice:
    print(f"Game is Tie, Your Point is: {y_point}")
else:
    print(f"'Congratulations!' You Won The Game, Your Points is: {y_point}" )

