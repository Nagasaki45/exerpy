Auto backup utility
===================

Write a script that get file name as argument. It checks if there is a file named ```filename_backup```. If there isn't it creates one. If there is it creates ```filename_backup01```, ```filename_backup02``` etc.

## Notes

You may need to use the following libraries:

- ```sys.argv```
- ```os.path```
- ```shutil```
- ```re```

## Template

	import os
	import sys
	import re
	import shutil


	def backup(filename):
	    # YOUR CODE HERE


	filename = sys.argv[1]
	backup(filename)
