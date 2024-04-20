#19,find a even number b/w 1 to n:
n=int(input("Enter Number :"))
i=2
while (i<=n):
    print(i)
    i=i+2

#second way to write or find :
n=int(input("Enter Number :"))
i=1
while (i<=n):
    if i%2==0:
        print(i)
    i=i+1
