#12,Write a to check no.is +/-/0:
a=int(input("Enter number :"))
if a>0:
    print("Number is positive")
elif a<0:
    print("Number is negative")
else:
    print("Zero")

#12,Write a program to find the middle number in a group of three number:
a=int(input("Enter 1st number :"))
b=int(input("Enter 2nd number  :"))
c=int(input("Enter 3rd nujmber :"))
if (a>b and a<c) or (a<b and a>c):
    print("Middle number =",a)
elif (b>a and b<c) or (b<a and b>c):
    print("Middle number =",b)
else:
        print("Middle number =",c)
