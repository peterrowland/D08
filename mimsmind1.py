#!/usr/bin/env python3
# mimsmin1.py

# GAME LOOP
# + setup max rounds = 2 ^ number length + length
# convert user input and secret to str
# setup counter

# If guess = secret, return game over win message.

# Else find bulls and cows

# def find_bulls(input, secret)
# bulls = 0
# for i in range(len(input)):
#   if input[0] == secret[0]:
#       bulls += 1
# return bulls

# def bull_scrub(input,secret)

# def find_cows(input, secret)
# cows = 0
# remove bulls from input and secret (bull_scrub)
# ? make list of unique numbers in (guess - bulls) ? sort?
# for each digit, if digit in (secret - bulls):
#   cows += Take the min() of count(guess - bulls) and count(secret-bulls)


##############################################################################
# Imports
import random
import sys
# Body

def get_secret(length):
    ''' Generates random number of n-digits specified by length parameter'''
    s = random.randint((10**(length - 1)), ((10**length) - 1))
    return str(s)


def get_bulls(guess, secret):
    ''' Finds all matching characters in both strings.
        returns count of "bulls" and their index in both lists'''
    bulls_count = 0
    bulls_index = []
    #listify()
    guess_lst = [x for x in guess]
    secret_lst = [x for x in secret]
    guess_no_bs = [x for x in guess]
    secret_no_bs = [x for x in secret]
    for i in range(len(guess_lst)):
        if guess_lst[i] == secret_lst[i]:
            bulls_count += 1
            bulls_index.append(i)

    return bulls_count, bulls_index


def listify(str):
    ''' Takes a string and returns a list '''
    lst = [x for x in str]
    return lst


def strip_bulls(lst, bulls_index):
    ''' Takes list and index, returns list with items at index turned to blanks '''
    for idx in bulls_index:
        lst[idx] = ''
    return lst


def return_unique(list_):
    ''' Returns list of unique digits in a string '''
    unique_list = []
    back = 0
    for i in range(len(list_)):
        if list_[i] not in unique_list:
            unique_list += list_[i]
    return unique_list


def get_cows(guess, secret):
    ''' Finds correct numbers in wrong position, after 'bulls' matches removed.
    up to # of occurences in secret.
    '''
    # Sets up return variable
    cows_count = 0

    # Gets results from bulls, assigns index to local var.
    bulls = get_bulls(guess, secret)
    bulls_index = bulls[1]

    # Removes bulls in local list variables using bulls index.
    guess_no_bs = strip_bulls(listify(guess), bulls_index)
    secret_no_bs = strip_bulls(listify(secret), bulls_index)

    # Gets unique digits out of guess_no_bs
    unique_guess_no_bs = return_unique(guess_no_bs)

    # Count loop
    for item in unique_guess_no_bs:
        guess_cows = guess_no_bs.count(item)
        secret_cows = secret_no_bs.count(item)
        cows_count += min(guess_cows, secret_cows)
    return cows_count


def mimsmind1(secret, length):
    '''Main Game Loop'''
    guess = ''
    guesses_total = (length**2) + (length - 1)
    guesses = guesses_total
    welcome_msg = "Let's play the mimsmind1 game. You have {} guesses.".format(guesses)
    prompt = 'Guess a {} digit number: '.format(length)
    print (welcome_msg + "\n" + prompt, end=' ')
    while guess == '':
        try:
            guess = input(' ')
            # guess_int = int(guess)
        except ValueError:
            print('Please enter only integers.')

        else:
            if len(guess) != length:
                print("Input must be {} digits long.".format(length))
                guess = ''

            else:
                # On match - display game over with number tries then exit
                if guess == secret:
                    print("You guessed it in {} tries.".format(guesses_total - guesses))
                    break
                # TO-DO: implement function calls.
                elif guesses > 0:
                    # Get
                    bulls = get_bulls(guess, secret)
                    count_bulls = bulls[0]
                    count_cows = get_cows(guess, secret)
                    guesses = guesses - 1

                    # Print Statment
                    print("{} bull(s), {} cow(s). Try again: ".format(count_bulls, count_cows))
                    guess = ''

                else:
                    print("Sorry, you ran out of guesses.")
                    break

##############################################################################
def main():
    # Try to convert command line to length, or default to 3
    try:
        length = int(sys.argv[1])
    except:
        length = 3

    # Set secret number of length
    secret = get_secret(length)

    # Start Game
    mimsmind1(secret, length)


if __name__ == '__main__':
    main()
