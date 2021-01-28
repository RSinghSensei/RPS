#Rock Paper Scissors
#Quick project to keep that github green
#Logic should be pretty simple
#User input implementation after or with starting?
import sys
from time import sleep
import random


compScore = 0
playerScore = 0
test2 = ["Rock", "Paper", "Scissors"]



def rps_init():
    global compScore
    global playerScore
    print("Alright, I'll assume you know the rules of the games");
    sleep(1)
    print("We have only 1 game mode currently, first to 3 points wins");
    sleep(1)
    print("Starting the game....");
    sleep(1)

    print("Rock\tPaper\tScissors")
    while playerScore < 3 and compScore < 3:
        test = input("Enter your choice: ")
        if test == "Rock":
            j = (random.choice(test2))
            print(j)
            if j == "Paper":
                print("Opponents Choice: Paper \n 1 point to computer")
                compScore+=1
                print(playerScore)
            elif j == "Rock":
                print("Computer player chose Rock as well, play again")
            elif j == "Scissors":
                print("Computer player chose Scissors, 1 point to you")
                playerScore+=1
                print(playerScore)
        if test == "Paper":
            k = (random.choice(test2))
            print(k)
            if k == "Paper":
                print("Computer player chose Paper as well, play again")
            elif k == "Rock":
                print("Computer player chose Rock, 1 point to you")
                playerScore+=1
                print(playerScore)
            elif k == "Scissors":
                print("Computer player chose Scissors, 1 point to computer")
                compScore+=1
                print(playerScore)
        if test == "Scissors":
            z = (random.choice(test2))
            print(z)
            if z == "Paper":
                print("Computer player chose Paper, 1 point to you")
                playerScore+=1
                print(playerScore)
            elif z == "Rock":
                print("Computer player chose Rock, 1 point to computer")
                compScore+=1
                print(playerScore)
            elif z == "Scissors":
                print("Computer player chose Scissors as well, play again")

    if playerScore == 3:
        print("Congratulations, you won! Play one more round?")
    elif compScore == 3:
        print("Tough luck, computer won this round. Wanna give it another try?")


print("Welcome to Ritvik's Rock Paper Scissors game")
while True:
    game_Init = input("Press ENTER to start a game, or Q to quit")
    if game_Init == "" \
                    "":
        print("Let's begin")
        break
    elif game_Init == "q" and "Q":
        print("Sad to see you go, please come back another time")
        sys.exit()
rps_init()












