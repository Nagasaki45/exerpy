import os
import sys
import re
import shutil


def backup(filename):
    # create backup filename and regex pattern
    backup_filename = '{}.backup'.format(filename)
    regex = re.compile(r'backup(?P<num>\d{2})$')
    # check if backup exist
    if os.path.isfile(backup_filename):
        # find the last backup
        max_backup = 0
        absdir = os.path.dirname(os.path.abspath(backup_filename))
        for f in os.listdir(absdir):
            result = regex.search(f)
            if result:
                this_backup = int(result.group('num'))
                if this_backup > max_backup:
                    max_backup = this_backup
        # set backup filename
        backup_filename += '{:02d}'.format(max_backup + 1)
    # create backup
    shutil.copyfile(filename, backup_filename)


filename = sys.argv[1]
backup(filename)
