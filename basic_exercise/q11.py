#! /usr/bin/python3
number= 7536
print("Given number ", number)

while (number>0):
    #get the last digit
    digit = number%10 

    #remove the last digit and repear the loop 
    number = number//10
    print(digit, end="")


