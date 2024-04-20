#12,Write a progarm to find percentage and grade in each marks:
a=int(input("Marks in math :"))
b=int(input("Marks in science :"))
c=int(input("Marks in s.s.t :"))
d=int(input("Marks in Hindi :"))
e=int(input("Marks in English :"))
total=a+b+c+d+e
percent=(total)/5
print("Total Marks =",total,"Percentage =",percent)
if percent>=80:
    print("You have got Grade A")
elif percent>=60:
    print("You got Grade B")
elif percent>=40:
    print("You got Gradee C")
else:
    print("You got Grade D")
