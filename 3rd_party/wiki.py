import random
import wikipedia
import webbrowser


def main():
    while True:
        user_input = raw_input('Which entry would you like to read about? ')
        try:
            page = wikipedia.page(user_input)
            break
        except wikipedia.exceptions.DisambiguationError as e:
            print('"{}" may refer to:'.format(user_input))
            for p in e.options:
                print(p)
    user_input = raw_input('Which you like to read the summary or redirect '
                           'to random reference? [summary | reference] ')
    if user_input == 'summary':
        print('{} summary:\n\n{}'.format(page.title, page.summary))
    else:
        ref = random.choice(page.references)
        webbrowser.open(ref)


if __name__ == '__main__':
    main()