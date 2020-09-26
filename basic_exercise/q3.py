#! /usr/bin/python3

def printNextone(str1):
    for i in range(len(str1)):
        if i%2 ==0:
            print(str1[i])

str1= "pynative"
print("Original String is ", str1)
print("Print only give index char")
printNextone(str1)
#printNextone("pynative")


str1= "I love PYTHON"

print ("\n")


print("Original String is ", str1)
print("Print only give index char")
printNextone(str1)
