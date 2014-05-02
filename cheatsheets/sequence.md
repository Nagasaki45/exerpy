Common sequence operations with examples
========================================

**`len`**
	
	:::python
	len('abc')  # -> 3

	len([1, 5, 2, 3])  # -> 4

**`in` / `not in`**

	:::python
	1 in [2, 1, 3]  # -> True

	'a' in 'hello world'  # -> False

	'a' not in 'hello world'  # -> True

**Slicing**

	:::python
	s = 'hello world'

	# slicing (inclusive start, exclusive end)
	s[1:4]  # -> 'ell'

	# from start to index
	s[:4]  # -> 'hell'

	# from index to end
	s[3:]  # -> 'lo world'

	# can use negative indexes as well
	s[2:-2]  # -> 'llo wor'

	# jumps
	s[::2]  # -> 'hlowrd'
	s[1::2]  # -> 'el ol'

	# negative jumps
	s[::-1]  # -> 'dlrow olleh'

**`+` and `*`**

	:::python
	[1, 2] + ['hello', 'world']  # -> [1, 2, 'hello', 'world']

	'hello ' + 'world'  # -> 'hello world'

	['a', 'b'] * 3  # -> ['a', 'b', 'a', 'b', 'a', 'b']

	'hello ' * 3  # -> 'hello hello hello '

**`min` / `max`**

	:::python
	l = [2, 1, 3]

	min(l)  # -> 1

	max(l)  # -> 3