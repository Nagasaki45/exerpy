def read_file(filename):
    with open(filename) as f:
        for line in f:
            yield line.strip()

palindromes = (w for w in read_file('wordsEn.txt') if w == w[::-1])
filtered = (w for w in palindromes if len(w) > 4)
print(len(list(filtered)))
