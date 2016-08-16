#!/usr/bin/env python3
# <filename>


##############################################################################
# Imports
import random
import sys

# Body

# generate random number of length or default length = 1
def get_secret(length):
    s = random.randint((10**(length - 1)), ((10**length) - 1))
    return s


def mimsmind0(secret, length):
    # BUG: breaking on shorter or longer entries
    guess = ''
    count = 0
    while guess == '':
        try:
            guess = input('Guess a {} digit number: '.format(length))
            guess_int = int(guess)
        except ValueError:
            print('Please enter only integers.')

        else:
            if len(guess) != length:
                print("Input must be {} digits long.".format(length))
                guess = ''

            else:
                if guess_int == secret:
                    count += 1
                    print("You guessed it in {} tries.".format(count))
                    break
                # lower
                elif guess_int < secret:
                    print("Higher.")
                    guess = ''
                    count += 1
                # higher
                else:
                    print("Lower.")
                    count += 1
                    guess = ''

##############################################################################
def main():
    try:
        length = int(sys.argv[1])

    except:
        length = 1
    secret = get_secret(length)
    mimsmind0(secret, length)

if __name__ == '__main__':
    main()
