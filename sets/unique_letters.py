def unique_letters_without_sets(words):
    chars = []
    unique_words = []
    for word in words:
        to_add = True
        for c in word:
            if c in chars:
                to_add = False
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
        if not word_set & chars:  # set intersection
            unique_words.append(word)
        chars |= word_set  # set union
    return ' '.join(unique_words)


l = [unique_letters_without_sets, unique_letters_with_sets]

for f in l:
    assert 'my is' == f(['my', 'name', 'is', 'john', 'doe'])
    assert 'hello back' == f(['hello', 'world!', 'hello', 'back'])
    assert 'once a' == f(['once', 'upon', 'a', 'time', 'my', 'dog'])
