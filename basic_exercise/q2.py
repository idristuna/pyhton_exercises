#! /usr/bin/python3

for i in range(10):
    if i == 0:
        print("Current number " + str(i) + " Previous number " + str(i) + " sum "+ str(i+i))
    else:    
        print("Current number " + str(i) + " Previous number " + str(i-1) + " sum "+ str(i+(i-1)))

