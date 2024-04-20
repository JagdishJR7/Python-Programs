# case insensitive camparision:

c='y'
while c=='y':
    s=input("Enetr a string:")
if s.upper()==s[::-1].upper():
    print("yes")
else:
    print("no")

c=input("continue (y/n)?")
