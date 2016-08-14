#!/usr/bin/env python3
# HW08_ch11_ex02b
# This borrows from exercise two in the book.
# Dictionaries have a method called keys that returns the keys of the
# dictionary, in no particular order, as a list.

# (1) Modify print_hist_old to print the keys and their values in alphabetical
# order.

# (2) Paste in your completed functions from HW08_ch11_ex02a.py

# (3) Within main() make the appropriate function calls to print the
# alphabetical histogram of pledge.txt
###############################################################################
# Imports


# Body
def get_pledge_list():
    """ Opens pledge.txt and converts to a list, each item is a word in
    the order it appears in the original file. returns the list.
    """
    with open('pledge.txt', 'r') as f:
        pledge_list = f.read().split()

    return pledge_list


def histogram_new(s):
    d = dict()

    for c in s:
        d[c] = 1

    for c in s:
        d[c] = (d.get(c)) + 1

    return d


def print_hist_old(h):
    a_dict = {}
    alpha = []
    for c in h:
        alpha.append(c)
    alpha.sort()
    for a in alpha:
        print("{} : {}".format(a, h[a]))


def print_hist_new(h):
    pass


###############################################################################
# INSERT COMPLETED CODE FROM HW08_ch11_ex02a BELOW: ###########################
###############################################################################


###############################################################################
# INSERT COMPLETED CODE FROM HW08_ch11_ex02a BELOW: ###########################
###############################################################################
def main():
    """ Calls print_hist_new with the appropriate arguments to print the
    histogram of pledge.txt.
    """
    print(print_hist_old(histogram_new(get_pledge_list())))


if __name__ == '__main__':
    main()
