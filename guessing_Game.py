import random

randomNum = random.randint(1,100)
guesses = 0
difficultyChois = 0
chosenGuess = int


print("Welcome to the Guess The Number game!")

print("Choose diffeculty by 1, 2, 3")
print("1. Easy (10 Guesses)")
print("2. Medium (5 Guesses)")
print("3. Hard (3 Guesses)")

print(randomNum)

while difficultyChois not in [1, 2, 3]:
    difficultyChois = int(input("Enter chosen diffeculty: "))
else:
    if difficultyChois == 1:
        guesses = 10
        print("You have chosen Easy!")
        print("You have 10 guesses left")
    elif difficultyChois == 2:
        guesses = 5
        print("You have chosen Medium!")
        print("You have 5 guesses left")

    elif difficultyChois == 3:
        guesses = 3
        print("You have chosen Hard!")
        print("You have 3 guesses left")

for i in range(guesses):

    chosenGuess = int(input("Choose your guessed number: "))
    remainingGuesses = guesses - i - 1

    if randomNum == chosenGuess:
        print("Right! Your guess is right")
        print("The random num was: ", randomNum)
        break
    elif randomNum > chosenGuess:
        print("Wrong! The secret number is higher then: ", chosenGuess)
    elif randomNum < chosenGuess:
        print("Wrong! The secret number is Lower then: ",  chosenGuess)
    if remainingGuesses > 0:
        print("You have ", remainingGuesses, "remaining guesses")
    else:
        print("You ran out of guesses!")

    


