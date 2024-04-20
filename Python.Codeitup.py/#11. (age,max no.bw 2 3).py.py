#11:Write a program to check the age is able to voting or not:
a=int(input("Enter your age :"))
if a>=18:
    print("Eligible to vote ")
else:
    print("Not eligible to vote")

#11.Write a program to find  max b/w two number:
a=int(input("Enter 1st number :"))
b=int(input("Enter 2nd number :"))
if a>b:
    print("Max Number =",a)
else:
    print("Max number =",b)


#11.Max number b/w three number:
a=int(input("Enter 1st number :"))
b=int(input("Enter 2nd number :"))
c=int(input("Enter 3rd number :"))
if a>b and a>c:
    print("Max number is =",a)
elif b>a and b>c:
    print("Max number is =",b)
else:
    print("Max number is =",c) 
