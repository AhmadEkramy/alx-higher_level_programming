#!/usr/bin/python3
def no_c(my_string):
    new_string = my_string.translate({ord(i): None for x in 'cC'})
    return new_string
