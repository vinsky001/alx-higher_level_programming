#!/usr/bin/python3
def print_reverse_alphabet():
    for i in range(ord('z'), ord('a') - 1, -1):
        if (i - ord('z')) % 2 == 0:
            print(chr(i).lower(), end="")
        else:
            print(chr(i).upper(), end="")
