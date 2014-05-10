'''
Based on Python for Data Analysis book, page 32.
'''

import os
import urllib
import zipfile
import pandas as pd
import matplotlib.pyplot as plt

NAMES_DIR = 'names'
URL = 'http://www.ssa.gov/oact/babynames/names.zip'


def download_and_extract(url, directory):
    print('Downloading archive...')
    filename, _ = urllib.urlretrieve(url)
    print('Extracting...')
    z = zipfile.ZipFile(filename)
    z.extractall(directory)

if not os.path.isdir(NAMES_DIR):
    os.mkdir(NAMES_DIR)
if not os.listdir(NAMES_DIR):
    download_and_extract(URL, NAMES_DIR)


def _load_tables():
    columns = ['name', 'sex', 'births']
    # 2012 is the last available year right now
    for year in xrange(1880, 2013):
        path = os.path.join(NAMES_DIR, 'yob{}.txt'.format(year))
        frame = pd.read_csv(path, names=columns)
        frame['year'] = year
        yield frame


def get_names():

    # concatenate everything into a single DataFrame
    return pd.concat(_load_tables(), ignore_index=True)


def main():

    names = get_names()

    # aggregate and plot births by year
    names.groupby('year').sum().plot()

    # similarily but with two lines, one for each gender
    names.pivot_table('births', rows='year', cols='sex', aggfunc=sum).plot()

    # analyze name trends
    total_births = names.pivot_table('births', rows='year', cols='name',
                                     aggfunc=sum)
    total_births[['Tom', 'Jacob', 'Alex']].plot()

    plt.show()


if __name__ == '__main__':
    main()
