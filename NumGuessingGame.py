# This is a number guessing game.

import random
print('Hi there! Please enter your name.')
name = input()

print('Hello, ' + name + ', Please guess a number between 1 and 20, you can try up to 5 times.')
GuessNum = random.randint(1, 20)

for timestaken in range(1, 6):
    print('Take a guess.')
    guess = int(input())

    if guess < GuessNum:
        print('Your guess is lower than expected.')
    elif guess > GuessNum:
        print('Your guess is higher than expected.')
    else:
        break # This condition is for the correct guess.

if guess == GuessNum:
    print('Good job, ' + name + ', the correct answer is ' + str(GuessNum) + ' and you finished in ' + str(timestaken) + ' times!')
else:
    print('You have tried 5 times, the correct answer was ' + str(GuessNum) +'.')
