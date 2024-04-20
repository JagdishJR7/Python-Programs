#8 ,armstrong number:
from math import *
num=int(input("enter the number :"))
a=0
n=0
i=num
while i!=0:
    i=int(i/10)
    n=n+1

i=num
while i!=0:
    remainder = i%10
    a= a+pow(remainder,n)
    i=int(i/10)

if (a==num):
    print("Armstrong no.")
else:
    print("Not a armstrong no.")
