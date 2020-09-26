#! /usr/bin/python3

def findEmma(str1):
    count = 0
    ls = str1.split(" ")
    for element in ls:
        if element == "Emma":
            count +=1
    print("Emma appeared ", count, " times ")

str1= "Emma is a good developer. Emma is writer"
        
findEmma(str1)
