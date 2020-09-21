#! /usr/bin/python3

def listPick(l1,l2):
    l3=[]
    for element in l1:
        if element%2 != 0:
            l3.append(element)
    for element in l2:
        if element%2 == 0:
            l3.append(element)
    print(l3)

l1 = [10,20,23,11,17]
l2 = [13,43,24,36,12]

listPick(l1,l2)
