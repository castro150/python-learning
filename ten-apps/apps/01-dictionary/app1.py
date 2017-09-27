import json
from difflib import get_close_matches

data = json.load(open('data.json'))


def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys(), cutoff=0.8)) > 0:
        similar = input('Did you mean %s instead? [Y/n]' % get_close_matches(word, data.keys(), cutoff=0.8)[0])
        if similar.lower() == 'y':
            return data[get_close_matches(word, data.keys(), cutoff=0.8)[0]]
        else:
            return 'The word does not exists. Please double check it.'
    else:
        return 'The word does not exists. Please double check it.'


def main():
    word = input('Enter word: ')

    output = translate(word)
    if type(output) == list:
        for item in output:
            print(item)
    else:
        print(output)


main()
