Overriding a method
===================

```calendar.TextCalendar``` is used to create string representations of a calendar.
Override one of its methods in order to change this representations as follows:
If the day is evenly divided by 7 or contains the character "7" in it replace it by "*".

## Notes
Browse the source!

## Template
	import calendar


	class MyTextCalendar(calendar.TextCalendar):

	    # --- WRITE YOUR CODE HERE --- #
	    pass
	    # ---------------------------- #


	c = MyTextCalendar()
	result = c.formatmonth(2014, 5)
	print(result)

	expected = '''      May 2014
	Mo Tu We Th Fr Sa Su
	          1  2  3  4
	 5  6  *  8  9 10 11
	12 13  * 15 16  * 18
	19 20  * 22 23 24 25
	26  *  * 29 30 31
	'''
	assert result == expected
