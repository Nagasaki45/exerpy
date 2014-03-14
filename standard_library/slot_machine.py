import random

money = 10
values = ['seven', 'cherry', 'crown', 'cake']

while money > 0:
    print('You have {}$'.format(money))
    ans = raw_input('Would you like to gamble? ')
    if ans != 'y':
        break
    triplet = [random.choice(values) for i in range(3)]
    print('Slot machine produced:\t|{:^10}|{:^10}|{:^10}|' \
        .format(*triplet))
    if (triplet[0] == triplet[1] == triplet[2]):
        money += 10
    elif not 'crown' in triplet:
        money -= 1

print('Game is finished, you have {}$.'.format(money))
