import random
number = str(random.randint(0,9))
print("Guess a number")
playing = True

while playing:
    guess = input("Enter an 1 digit number")
    if number == guess:
        print("You guessed it right")
        break
    else:
        print("You guessed it wrong")
        