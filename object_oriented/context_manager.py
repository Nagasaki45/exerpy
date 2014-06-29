from __future__ import print_function
import time


class Profiler(object):

    template = '{} seconds this run, total of {} seconds'

    def __init__(self):
        self.sum = 0

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        current = time.time() - self.start
        self.sum += current
        print(self.template.format(current, self.sum))

    def elapsed(self):
        current = time.time() - self.start
        total = self.sum + current
        print('elapsed:', self.template.format(current, total))


profiler = Profiler()

# start running the profiler
with profiler:
    for i in xrange(10000000):
        if i == 2939232:
            profiler.elapsed()

time.sleep(2)

# continue with the same profiler
with profiler:
    for i in xrange(10000000):
        if i == 5982143:
            profiler.elapsed()

# start another profiler, using the with __ as __ syntax
with Profiler() as another_profiler:
    for i in xrange(10000000):
        pass
