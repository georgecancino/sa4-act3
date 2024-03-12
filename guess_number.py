number = 10

print("I'm thinking of a number...")

while True:
    guess = input("What number am I thinking of? ")

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
    else:
        print("Sorry! Incorrect guess. Try again.")
