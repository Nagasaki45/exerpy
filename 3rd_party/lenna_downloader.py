import urllib
import os

URL = 'http://upload.wikimedia.org/wikipedia/en/2/24/Lenna.png'
FILENAME = 'lenna.jpg'


def do():
    if FILENAME in os.listdir('.'):
        return
    print('downloading lenna image to "{}"'.format(FILENAME))
    urllib.urlretrieve(URL, FILENAME)

if __name__ == '__main__':
    do()
