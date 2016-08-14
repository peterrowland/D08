#!/usr/bin/env python3
# HW08_ch11_ex01
# Write a function that reads the words in words.txt and stores them as keys
# in a dictionary (returning the dictionary). It doesn’t matter what the
# values are. Then you can use the in operator as a fast way to check whether
# a string is in the dictionary.
###############################################################################
# Imports


# Body
def load_words():
    fin = open('words.txt', 'r')
    words = fin.readlines()
    for i in range(len(words)):
        words[i].strip()

    return words


def store_to_dict():
    words = load_words()
    d = {}
    for word in words:
        d[word.strip()] = ''
    return d

###############################################################################


def main():  # DO NOT CHANGE BELOW
    words_dict = store_to_dict()
    if "this" in words_dict:
        print("Yup.")
    if "qwertyuiop" in words_dict:
        print("Hmm.")

if __name__ == '__main__':
    main()
