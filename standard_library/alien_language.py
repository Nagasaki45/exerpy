import re

words = ['abc', 'bca', 'dac', 'dbc', 'cba']


def num_of_options(pattern, words):
    regex = re.compile('^{}$'.format(pattern))
    counter = 0
    for word in words:
        if regex.search(word):
            counter += 1
    return counter


assert 2 == num_of_options('[ab][bc][ca]', words)
assert 1 == num_of_options('abc', words)
assert 3 == num_of_options('[abc][abc][abc]', words)
assert 0 == num_of_options('[zyx]bc', words)
