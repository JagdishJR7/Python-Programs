#1 program:
name="Jagdish"
print("Hello",name,"Welcome in the coding life")

#2 Square root program in the python:
a=int(input("Enter the number :"))
b=a**0.5
print("square root is :",b)

#3 cube root of a number :
a=int(input("Enter the number:"))
b=a**(1/3)
print("cube root of a number :",b)

#or
def cube_root(x):
    return x**(1/3)
a=int(input("Enter the number :"))
cube_root(a)
print(cube_root(a))

#4,fahrenheit to celcius (conveter):
temp=float(input("Enter temp in fahrenheit: "))
celcius= (temp - 32)*5/9
print(f"{temp} in fahrenheit is equal to the {celcius} in celcius ")

#5, Area of triangle:
a=float(input("Enter the height of the  triangle :"))
b=float(input("Enter the base of the triangle:",))
Area=1/2*(a*b)
print("Area of the triangle is:",Area,"unit")

#6 , Area of circle:
a=float(input("enter the radius of circle :"))
b= 3.14*a*a
print("Area of circle is:",b)

# calculator:
a=float(input("enter the 1st no."))
b=float(input("enter the 2nd no."))
c=a*b
print("multyplication of  a number is :",c)
