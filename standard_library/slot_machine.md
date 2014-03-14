Slot machine
============

Create a slot maching. The slot machine will randomly generate a triplet from the values:
[seven, cherry, crown, cake]. The player will start gambling with 10$. Ask the player if he wants to play before each "round". Every time the player will spend 1$. If the slot machine product a triplet with the same value he win 10$, if the triplet contains a crown he won't loose his bet, else he loose the 1$.

## Notes

You may need to use the following libraries:

- ```random.choice```

## Template

	import random

	money = 10
	values = ['seven', 'cherry', 'crown', 'cake']

	while money > 0:
	    # YOUR CODE HERE
	    
	print('Game is finished, you have {}$.'.format(money))
