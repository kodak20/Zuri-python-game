import random

while True:
    user_choose = input("Enter a choice (rock, paper, scissors): ")
    possible_choices = ["rock", "paper", "scissors"]
    computer_chooses = random.choice(possible_choices)
    print(f"\nYou chose {user_choose}, computer chose {computer_chooses}")
        
    if user_choose == computer_chooses:
        print(f"Both players selected {user_choose}. It's a tie!")
    elif user_choose == "rock":
        if computer_chooses == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_choose == "paper":
        if computer_chooses == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose")
    elif user_choose == "scissors":
        if computer_chooses == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes Scissors! You lose")
            
    play_once_more = input("Do you want to play again? (y/n): ")
    if play_once_more.lower() != "y":
        break