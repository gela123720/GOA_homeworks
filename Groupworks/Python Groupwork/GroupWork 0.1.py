import random

options = ["rock" , "paper" , "scissors"]
playing = True

while playing:

    player = None
    bot = random.choice(options)

    while player not in options:
        player = input("Choose an option (rock , paper , scissors): ")

    print("Player: " + player)
    print("Bot: " + bot)

    if player == bot:
        print("Tie!")

    elif player == "rock" and bot == "scissors":
        print("you win!")

    elif player == "paper" and bot == "rock":
        print("you win!")

    elif player == "scissors" and bot == "paper":
        print("you win!")

    else:
        print("you lose!")

    if not input("Play Again? (y/n): ").lower() == "y":
        playing = False

print("Thanks For Playing!")