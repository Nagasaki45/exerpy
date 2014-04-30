'''
Example of inheritance, method overriding (by knockout),
and usage of mixins.
'''

from six import unichr


class Deck(object):

    SUIT = [('S', 'Spades'),
            ('H', 'Hearts'),
            ('D', 'Diamonds'),
            ('C', 'Clubs')]
    SUIT_NAMES = dict(SUIT)
    VALUES = ['0', 'Ace'] + [str(i) for i in range(2, 11)] + ['Jack',
                                                              'Queen',
                                                              'King']

    def __init__(self):
        self.cards = [(t[0], v) for t in self.SUIT
                      for v in range(1, 14)]

    def render(self):
        return u', '.join(self.render_card(c) for c in self.cards)

    def render_card(self, card):
        return u'{} of {}'.format(self.VALUES[card[1]],
                                  self.SUIT_NAMES[card[0]])

print('Deck\n====')
deck = Deck()
print(deck.render())
print('')


class HtmlDeck(Deck):

    def render(self):
        out = ['<html><head><title>Html unicode deck</title></head><body>']
        out.append('<ul>')
        for c in self.cards:
            out.append(u'<li>{}</li>'.format(self.render_card(c)))
        out.append('</ul>')
        out.append('</body></html>')
        return u'\n'.join(out)


print('Html deck\n=========')
html_deck = HtmlDeck()
print(html_deck.render())
print('')


class UnicodeRenderMixin(object):

    def render_card(self, card):
        base = 0x1F0A0
        suit_index = [s[0] for s in self.SUIT].index(card[0])
        final = base + suit_index * 0x10 + int(card[1] if card[1] < 12
                                               else card[1] + 1)
        return unichr(final)


class UnicodeDeck(UnicodeRenderMixin, Deck):
    pass


class HtmlUnicodeDeck(UnicodeRenderMixin, HtmlDeck):
    pass


print('Unicode deck\n============')
unicode_deck = UnicodeDeck()
print(unicode_deck.render())
print('')

print('Unicode html deck\n=================')
html_unicode_deck = HtmlUnicodeDeck()
print(html_unicode_deck.render())
print('')
