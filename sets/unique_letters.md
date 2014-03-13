Unique letters
==============

Get a list of words. Return a string that contains only the words with letter that doesn't present in previous words of the list.

Solve once using lists and once with higher level set operations.

## Template
	def unique_letters_without_sets(words):
		# YOUR CODE HERE


	def unique_letters_with_sets(words):
	    # YOUR CODE HERE


	l = [unique_letters_without_sets, unique_letters_with_sets]

	for f in l:
	    assert 'my is' == f(['my', 'name', 'is', 'john', 'doe'])
	    assert 'hello back' == f(['hello', 'world!', 'hello', 'back'])
	    assert 'once a' == f(['once', 'upon', 'a', 'time', 'my', 'dog'])
