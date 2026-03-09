import random

def guessing_game():
    print(" Number Guessing Game")
    print("Rules: Guess the number between 1 and 20")

    number = random.randint(1, 20)
    attempts = 0

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < number:
            print("Too Low! Try again.")
        elif guess > number:
            print("Too High! Try again.")
        else:
            print(f" Correct! You guessed in {attempts} attempts.")
            break

# Start Game
guessing_game()
