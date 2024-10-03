##easier version of the game
import random

def game():
    user_score = 0
    computer_score = 0

    while True:
        print("\nCurrent Score:")
        print(f"You: {user_score}")
        print(f"Computer: {computer_score}")

        if user_score == 3:
            print("\nYou win!")
            break
        elif computer_score == 3:
            print("\nComputer wins!")
            break

        user_move = input("\nEnter your move (rock/paper/scissors or r/p/s): ").lower()

        while user_move not in ["rock", "paper", "scissors", "r", "p", "s"]:
            user_move = input("Invalid move. Please enter rock, paper, or scissors (or r, p, s): ").lower()

        if user_move in ["r", "p", "s"]:
            move_map = {"r": "rock", "p": "paper", "s": "scissors"}
            user_move = move_map[user_move]

        moves = ["rock", "paper", "scissors"]
        computer_move = random.choice(moves)

        print(f"\nYou chose: {user_move}")
        print(f"Computer chose: {computer_move}")

        if user_move == computer_move:
            print("It's a tie!")
        elif (user_move == "rock" and computer_move == "scissors") or \
             (user_move == "paper" and computer_move == "rock") or \
             (user_move == "scissors" and computer_move == "paper"):
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

game()
