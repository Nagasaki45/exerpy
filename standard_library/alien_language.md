Alien language
==============

(Simplified version of [this problem](https://code.google.com/codejam/contest/90101/dashboard))

After years of study, scientists have discovered an alien language transmitted from a faraway planet.

Unfortunately, some of the received signals are weakened due to the distance between our two planets and some of the words may be misinterpreted. In order to help them decipher these messages, the scientists have asked you to devise an algorithm that will determine the number of possible interpretations for a given pattern.

Each token in a pattern is either a single lowercase letter or a group of unique lowercase letters surrounded by square braces [ and ]. For example: ```[ab]d[dc]``` means the first letter is either a or b, the second letter is definitely d and the last letter is either d or c. Therefore, the pattern ```[ab]d[dc]``` can stand for either one of these 4 possibilities: add, adc, bdd, bdc.

Create a function that receive a pattern as described above and a list of words that creates the alien language dictionary. The function should return the number of possible words the pattern can satisfy.

## Notes

You may need to use the following libraries:

- ```re```

## Template

	import re

	words = ['abc', 'bca', 'dac', 'dbc', 'cba']


	def num_of_options(pattern, words):
	    # YOUR CODE HERE


	assert 2 == num_of_options('[ab][bc][ca]', words)
	assert 1 == num_of_options('abc', words)
	assert 3 == num_of_options('[abc][abc][abc]', words)
	assert 0 == num_of_options('[zyx]bc', words)
