
#12, convert binary to decimal:
b_numb = list(input("Enter a binary number :"))
value = 0
for i in range(len(b_numb)):
    digit = b_numb.pop()
    if digit == '1':
        value = value + pow(2,i)

print("The decimal value of the number is",value)
