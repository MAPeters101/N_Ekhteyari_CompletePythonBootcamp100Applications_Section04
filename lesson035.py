import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!!")
    target_number = random.randint(1, 100)
    attempts = 0

    try:
        while True:
            user_guess = int(input("Guess the number (1-100): "))
            attempts += 1

            if user_guess == target_number:
                print(f"Congratulations! You guessed the correct number {target_number} in {attempts} attempts.")
                break
            elif user_guess < target_number:
                print("Too low, try again.")
            else:
                print("Too high, try again.")
    except ValueError:
        print("Error: Please enter a valid number.")


number_guessing_game()






