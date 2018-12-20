#!/bin/python3

N = int(input())
if(N%2==1 or (N%2==0 and N in list(range(6,21)))):
    print("Weird")
elif(N%2==0 and (N in list(range(2,6)) or N>20)):
    print('Not Weird')
else:
    print("nothing")
