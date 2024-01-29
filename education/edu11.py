secret_number=9
guess_count=0
guess_limit=3
while guess_count< guess_limit:
    guess=int(input("Guess the number : "))
    if guess == secret_number:
        print("Congratulations! You guessed the number correctly!")
        break
    else:
        guess_count += 1
        print(f"Sorry you couldn't guess.Try again. You have {guess_limit-guess_count} guesses left.")
        if guess_count==guess_limit:
            print("Sorry you have no guess limit left.")
            break


