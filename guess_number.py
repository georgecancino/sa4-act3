number = 10
total_guesses = 3

print("I'm thinking of a number...")

for attempt in range(total_guesses):
    guesses_left = total_guesses - attempt
    guess = input(f"What number am I thinking of? You have {guesses_left} guesses left. ")

    if guess.lower() == 'q':
        print(f"The number was {number}.")
        break

    try:
        guess = int(guess)
    except ValueError:
        print("Try again")
        continue

    if guess == number:
        print("Congratulations! You guessed the right number.")
        break
    elif guess < number:
        print("Sorry! Your guess is too low.")
    else:
        print("Sorry! Your guess is too high.")

else:
    print(f"Sorry! You ran out of guesses. The number was {number}.")
