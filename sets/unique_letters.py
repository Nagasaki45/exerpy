def unique_letters_without_sets(words):
    chars = []
    unique_words = []
    for word in words:
        to_add = False
        for c in word:
            if not c in chars:
                to_add = True
                break
        if to_add:
            unique_words.append(word)
        [chars.append(c) for c in word]
    return ' '.join(unique_words)


def unique_letters_with_sets(words):
    chars = set()
    unique_words = []
    for word in words:
        word_set = set([c for c in word])
        if word_set - chars:  # set difference
            unique_words.append(word)
        chars |= word_set  # set union
    return ' '.join(unique_words)


l = [unique_letters_without_sets, unique_letters_with_sets]

for f in l:
    assert 'a ab ac' == f(['a', 'a', 'ab', 'b', 'ac', 'abc'])
    assert 'my name is john doe' == f(['my', 'name', 'is', 'john', 'doe'])
    assert 'hello world! back' == f(['hello', 'world!', 'hello', 'back'])
    assert 'once upon a time dog' == f(['once', 'upon', 'a', 'time', 'dog', 'ate', 'cat'])
