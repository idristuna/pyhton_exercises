#! /usr/bin/python3

def printNextone(str1):
    for i in range(0, len(str1)-1, 2 ):
        print ("index[",i,"]", str1[i])

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
