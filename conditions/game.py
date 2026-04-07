import random

SYSTEM_MOVES = [
    "rock",
    "paper",
    "scissors"
]

player_move = input("Enter your move (rock, paper, scissors): ")

system_move = random.choice(SYSTEM_MOVES)

if player_move == system_move:
    print("It's a tie!")
elif player_move == "rock" and system_move == "scissors":
    print("You win!")
    print(f"System move: {system_move}")
elif player_move == "paper" and system_move == "rock":
    print("You win!")
    print(f"System move: {system_move}")
elif player_move == "scissors" and system_move == "paper":
    print("You win!")
    print(f"System move: {system_move}")
else:
    print("You lose!")
    print(f"System move: {system_move}")
