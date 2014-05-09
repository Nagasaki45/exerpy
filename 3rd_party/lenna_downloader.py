import urllib
import os

URL = 'http://upload.wikimedia.org/wikipedia/en/2/24/Lenna.png'
FILENAME = 'lenna.jpg'

if not FILENAME in os.listdir('.'):
    print('downloading lenna image to "{}"'.format(FILENAME))
    urllib.urlretrieve(URL, FILENAME)
