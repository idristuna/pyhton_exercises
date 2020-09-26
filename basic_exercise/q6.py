#! /usr/bin/python3

def isDivisible_by_Five(list1):
    for element in list1:
        if element%5 == 0:
            print(element)


list1 = [10,20,33,46,55]


#print(isDivisible_by_Five(list1))
isDivisible_by_Five(list1)

