import random
from PIL import Image

# make sure lenna.png is available in directory
import lenna_downloader

PIECES = 10
FILENAME = 'lenna.jpg'
PAZZLE = 'pazzle.jpg'


def main():
    im = Image.open(FILENAME)
    piece_width = im.size[0] / PIECES
    piece_height = im.size[1] / PIECES
    regions = [(x, y) for x in range(PIECES) for y in range(PIECES)]
    random.shuffle(regions)
    new = Image.new(im.mode, im.size)
    for i, (x, y) in enumerate(regions):
        piece = im.crop(bounderies(x, y, piece_width, piece_height))
        row, col = divmod(i, PIECES)
        new.paste(piece, bounderies(row, col, piece_width, piece_height))
    new.save(PAZZLE)

def bounderies(x, y, width, height):
    '''Returns left, top, right and bottom.'''

    return x * width, y * height, (x + 1) * width, (y + 1) * height


if __name__ == '__main__':
    main()