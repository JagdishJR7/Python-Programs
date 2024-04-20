#10, fibonacci series:
def FiboRecursion(n):
    if n<=1:
        return n
    else:
        return(FiboRecursion(n-1) + FiboRecursion(n-2))

nterms = int(input("Enter the terms:"))
if nterms <=0:
    print("Please enter a positive integer")
else:
    print("Fibonaccci series :")
    for i in range(nterms):
        print(FiboRecursion(i));

