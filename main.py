#Rock Paper Scissors
#Quick project to keep that github green
#Logic should be pretty simple
#User input implementation after or with starting?
import sys
from time import sleep
import random


compScore = 0
playerScore = 0
c_ops = ["Rock", "Paper", "Scissors"]


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
    while playerScore != 3 and compScore!=3:
        userchoice = input("Enter your choice")
        if userchoice == "Rock":
            if random.choice(c_ops) == "Paper":
                print("Computer player chose Paper, 1 point to computer")
                compScore+=1
            elif random.choice(c_ops) == "Rock":
                print("Computer player chose Rock as well, play again")
            elif random.choice(c_ops) == "Scissors":
                print("Computer player chose Scissors, 1 point to you")
                playerScore+=1
        if userchoice == "Paper":
            if random.choice(c_ops) == "Paper":
                print("Computer player chose Paper as well, play again")
            elif random.choice(c_ops) == "Rock":
                print("Computer player chose Rock, 1 point to you")
                playerScore+=1
            elif random.choice(c_ops) == "Scissors":
                print("Computer player chose Scissors, 1 point to computer")
                compScore+=1
        if userchoice == "Scissors":
            if random.choice(c_ops) == "Paper":
                print("Computer player chose Paper, 1 point to you")
                playerScore+=1
            elif random.choice(c_ops) == "Rock":
                print("Computer player chose Rock, 1 point to computer")
                compScore+=1
            elif random.choice(c_ops) == "Scissors":
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












