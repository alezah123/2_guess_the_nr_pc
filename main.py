
import random

def guess(x):

    nr = random.randint(1,x)
    guess = 0
    while guess != nr:
        guess = int(input("Enter you guess: "))

        if guess > nr:
            print("Too high")
        elif guess < nr:
            print("too low")

    print(f"You guessed it!! It's {nr}")

def comp_guess(low,high):
    print("The computer will try to guess your nr")
    print("Please enter 'l' for low, 'h' for high and 'c' for correct")
    clue = 'x'

    while clue != 'c':
        if low != high:
            guess = random.randint(low, high)
            print(f"Is it {guess}?")
            clue = input("Please enter your clue: ".lower())
            if clue == 'l':
                low = guess + 1
            elif clue == 'h':
                high = guess -1
        elif low == high:
            clue = 'c'
            guess = low

    print(f"I have guessed it!!! it's {guess}")


if __name__ == '__main__':
    # x = int(input("Please guess the number between 1 and: "))
    # guess(x)

    comp_guess(1,16)



