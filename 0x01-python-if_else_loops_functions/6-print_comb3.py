#!/usr/bin/python3
for num in range(10):
    for j in range(num+1, 10):
        print("{}, {}".format(num, j), end=", ")
print("\b\b\n")
