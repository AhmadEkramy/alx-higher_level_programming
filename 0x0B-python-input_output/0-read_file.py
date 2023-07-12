#!/usr/bin/python3
"""
The read_file function is inside
"""


def read_file(filename=""):
    """""reads a text file and prints it"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
