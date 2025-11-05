import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print("Too low! guess again")
        elif guess > random_number:
            print("Too high! guess again")
    print(f"You guessed({random_number}) correctly!")

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    print(f"choose a number between 1 and {x}")
    while feedback != 'y':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low #it could be high too

        feedback = input(f'Is {guess} too high(H), too low(L) or right(y)?: ').lower()
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1

    print(f"computer guessed({guess}) correctly!")

computer_guess(10)