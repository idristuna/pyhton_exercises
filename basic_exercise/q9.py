#! /usr/bin/python3
def checkReverse(num1):
    if str(num1)==str(num1)[::-1]:
         print("Original and reverse is same")
    else:
        print("Original and reverse not same")

checkReverse(121)
checkReverse(453)
