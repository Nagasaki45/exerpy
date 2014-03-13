Unique letters
==============

Get a list of words. Return a string that contains only the words with at least one letter that wasn't present in previous words of the list.

Solve once using lists and once with higher level set operations.

## Template
	def unique_letters_without_sets(words):
		# YOUR CODE HERE


	def unique_letters_with_sets(words):
	    # YOUR CODE HERE


	l = [unique_letters_without_sets, unique_letters_with_sets]

	for f in l:
	    assert 'a ab ac' == f(['a', 'a', 'ab', 'b', 'ac', 'abc'])
	    assert 'my name is john doe' == f(['my', 'name', 'is', 'john', 'doe'])
	    assert 'hello world! back' == f(['hello', 'world!', 'hello', 'back'])
	    assert 'once upon a time dog' == f(['once', 'upon', 'a', 'time', 'dog', 'ate', 'cat'])

