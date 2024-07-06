import random

def guess_the_number():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Guess the Number Game!")
    print("I'm thinking of a number between 1 and 100. Can you guess what it is?")

    while True:
        # Prompt the user to input their guess
        user_guess = input("Enter your guess: ")

        # Check if the input is a valid number
        if not user_guess.isdigit():
            print("Invalid input! Please enter a valid number.")
            continue

        # Convert the input to an integer
        user_guess = int(user_guess)
        attempts += 1

        # Provide feedback on the guess
        if user_guess < number_to_guess:
            print("Too low! Try again.")
        elif user_guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number correctly in {attempts} attempts.")
            break

# Run the game
guess_the_number()
