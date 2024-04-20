#14 prime no. upto 100 no.:
n=1
while(n<=100):
    count=0
    i=2

    while(i<=n//2):
        if(n%i==0):
            count = count + 1
        i=i+1

    if (count == 0 and n!=1):
        print(" %d" %n, end=' ')
    n=n+1
