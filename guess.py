import random

print("Welcome to the Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
number = random.randint(1, 100)
if input("Choose a difficulty 'easy' or 'hard': ") == "easy":
    guesses = 10
else:
    guesses = 5

got_it = False
while not got_it:
    if guesses > 0:
        print(f"You have {guesses} remaining.")
        player_guess = int(input("Make a guess: "))
        if player_guess == number:
            print(f"You got it! The number was {number}")
            got_it = True
        elif player_guess < number:
            print("Too low.\nGuess again.")
            guesses -= 1
        else:
            print("Too high.\nGuess again.")
            guesses -= 1
    else:
        got_it = True
        print("You've run out of guesses, you lose.")
