#! /usr/bin/python3
def exponent(base, exp):
    result = 1

    for i in range(exp):
        result *= base
    print(result)

exponent(3, 4)
