#! /usr/bin/python3
# Read line 4 from give file
with open("test.txt", "r") as fp:
    lines = fp.readlines()
    print(lines[3])
