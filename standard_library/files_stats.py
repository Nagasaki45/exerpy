import sys


def file_stats(filename):
    print('{:14}{}'.format('File:', filename))
    # read the file
    with open(filename) as f:
        lines = f.read().splitlines()
    # print number of lines, ignoring empty lines
    lines = [l for l in lines if l]
    print('    {:10}{}'.format('Lines:', len(lines)))
    # print number of words
    words = []
    [[words.append(w) for w in l.split()] for l in lines]
    print('    {:10}{}'.format('Words:', len(words)))
    # print number of alpha numeric characters
    chars = []
    [[chars.append(c) for c in w if c.isalpha()] for w in words]
    print('    {:10}{}'.format('Chars:', len(chars)))


for filename in sys.argv[1:]:
    file_stats(filename)
