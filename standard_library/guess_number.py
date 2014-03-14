import random

max_guesses = 6
guesses_made = 0

number = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')

while guesses_made < max_guesses:
    guess = int(raw_input('Take a guess: '))
    guesses_made += 1
    if guess == number:
        break

    if guess < number:
        print('Your guess is too low.')
    else:
        print('Your guess is too high.')

if guess == number:
    print("Good job! You've guessed my number in {} guesses!" \
        .format(guesses_made))
else:
    print('Nope. The number I was thinking of was {}'.format(number))
