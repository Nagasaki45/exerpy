Writing a profiler using the context manager protocol
=====================================================

Write a Profiler class that implements the [context manager protocol](https://docs.python.org/2/reference/datamodel.html#with-statement-context-managers). The profiler will measure the time of the with block execution and will print the total runtime of the profiler as well as the current block execution time upon exiting from the block.

In addition, implement a ``elapsed`` method that will trigger similar print manually.

## Template

	class Profiler(object):

	    # --- WRITE YOUR CODE HERE --- #
	    pass
	    # ---------------------------- #


	profiler = Profiler()

	# start running the profiler
	with profiler:
	    for i in xrange(10000000):
	        if i == 2939232:
	            profiler.elapsed()

	# continue with the same profiler
	with profiler:
	    for i in xrange(10000000):
	        if i == 5982143:
	            profiler.elapsed()

	# start another profiler, using the with __ as __ syntax
	with Profiler() as another_profiler:
	    for i in xrange(10000000):
	        pass
