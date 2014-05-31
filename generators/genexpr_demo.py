# The syntax is very similar to list comprehension:
my_gen = (i**2 for i in range(20) if i % 3 == 0)
next(my_gen)  # -> 0
next(my_gen)  # -> 9
next(my_gen)  # -> 36
# ...

# Some of the advantages of using generators (and iterators in general)
# are laziness and low memory usage.

# Without generators
def is_prime(x):
    return not any([x % k == 0 for k in range(2, x)])

# The list comprehension inside could take a long time to finish although
# the first truthy value will indicate the result of the function.
# %timeit is_prime(1000000) -> 167 ms


# with generators
def is_prime_lazy(x):
    return not any(x % k == 0 for k in range(2, x))

# any will consume the generator expression and will return on first true.
# %timeit is_prime_lazy(1000000) -> 1.6 microseconds

# Generators can consume other generators to create a pipeline.
# In the examples below the goal is to read a log, filter only requests
# with status code of 200, and sum the bytes of those requests.

# without generators
with open('access-log') as f:
    lines = f.read().splitlines()
total = 0
for line in lines:
    code, bytes = line.strip().split()[-2:]
    if code == '200' and bytes != '-':
        total += int(bytes)
print('Total bytes requested: {}'.format(total))

# using generators
with open('access-log') as f:
    rows = (line.strip() for line in f)
    only_200 = (r for r in rows if r.split()[-2] == '200')
    bytes_column = (r.split()[-1] for r in only_200)
    bytes = (int(b) for b in bytes_column if b != '-')
    print('Total bytes requested: {}'.format(sum(bytes)))

# note that in the example above only the "sum" function triggered the
# processing of the data through the pipeline!
