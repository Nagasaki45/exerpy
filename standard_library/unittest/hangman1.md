Test Driven Hangman game Development (with unittests)
=====================================================

Create a class based hangman game with unittest!

Example:

	game = Hangman("hello", 10)  # "hello" is the secret word, there are 10 tries
	print game.status()  # -> ?????

Start from writing a test to validate that the length of ``game.status()`` must be equal to the length of the secret word but replaced with question marks. **Only after writing the tests** start to implement the ``Hangman`` class. Run the test until it passed.

## Templates

in ``hangman_tests.py``

	import unittest
	from hangman import Hangman

	class TestSequenceFunctions(unittest.TestCase):

	    def initial_status(self):
	        # ----- ENTER SOME CODE HERE --------
	        pass
	        # -----------------------------------

	if __name__ == '__main__':
	    unittest.main()

in ``hangman.py``
	
	class Hangman(object):

	    def __init__(self, secret_word, tries):
	        # ----- ENTER SOME CODE HERE --------
	        pass
	        # -----------------------------------

	    def status(self):
	        # ----- ENTER SOME CODE HERE --------
	        pass
	        # -----------------------------------
