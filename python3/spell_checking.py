# python build in module
import difflib
from PyDictionary import PyDictionary

words = ['i', 'love', 'like', 'absent', 'Bangladesh', 'money']

# function that find closer word
def word_check(s):
    for word in s.casefold().split():
        if word not in words:
            suggestion = difflib.get_close_matches(word, words)
            if len(suggestion) != 0:
                print(f'Did you mean {", ".join(str(x) for x in suggestion)} instead of {word}?')
            else:
                print("Not find any error")

s = input('Input a string: ')
word_check(s)
