# PYTHON ROCK PAPER SCISSOR GAME
import random

options = ("rock", "paper", "scissor")  # Tuple
playing = True
while playing:
    player = None
    computer = random.choice(options)
    while player not in options:    
        player = input("Enter your choice (rock, paper, scissor) : ").lower()

    print(f"Player : {player}")
    print(f"Computer : {computer}")

    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scissor":
        print("Your win!")
    elif player == "paper" and computer == "rock":
        print("Your win!")
    elif player == "scissor" and computer == "paper":
        print("Your win!")
    else:   
        print("Your lose!")
    if not input("Play again? (y/n) : ").lower() == "y":
        playing = False

print("Thanks for playing!")