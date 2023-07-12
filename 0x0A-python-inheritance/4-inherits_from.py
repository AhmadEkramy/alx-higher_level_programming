#!/usr/bin/python3
"""
The inherits_from is inside
"""


def inherits_from(obj, a_class):
    """returns true if obj is a subclass of a_class else return false"""
    return(issubclass(type(obj), a_class) and type(obj) != a_class)
