import random

# player 1
print('Player 1\n========')
word = raw_input('Enter a word -> ')
as_list = list(word.lower())
random.shuffle(as_list)
shuffled = ''.join(as_list)
print(shuffled)

# player 2
print('\n' * 100 + 'Player 2\n========')
tries = 0

while tries < 4:
    ans = raw_input(
        'What word has been shuffled to give {} -> '.format(shuffled)
    )
    if ans == word:
        break
    print('Nope, try again')
    tries += 1

if tries == 4:
    print('Game over!')
else:
    print("Good job! You've find out the word in {} tries".format(tries))
