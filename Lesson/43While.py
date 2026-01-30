correctNumber = 7
userGuess = 0
while userGuess != correctNumber:
    userGuess = int(input("Please guess a number : "))
    if userGuess > correctNumber:
        print("You guessed too high!")
    elif userGuess < correctNumber:
        print("You guessed too low!")
    else:
        print("Congratulations! You guessed the correct number.")