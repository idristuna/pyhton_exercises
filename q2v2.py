#! /usr/bin/python3

def sumNum(num):
    previousNum = 0
    for i in range(num):
        sum = previousNum + i
        print("Current number ", i,  " Previous number ", previousNum, " sum ", sum )
        previousNum = i 
print("Printing current and previosu number and sum give range(10)")
sumNum(10)

print("\n")

print("Printing current and previosu number and sum give range(20)")
sumNum(20)

