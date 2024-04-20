#9, palindrome no. ;
n=int(input("Enter the number :"))
i=n
rev=0
while n>0:
    dig=n%10
    rev=(rev*10)+dig
    n=n//10
if (i==rev):
    print("The number is Palindrome no.")
else:
    print("The number is not a palindrome no.")
