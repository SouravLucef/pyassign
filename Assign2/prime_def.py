def prime(n):
    for i in range(2,n//2+1):
        if(n%i==0):
            return 0
    return 1

for i in range(3,1001):
    if(prime(i) and prime(i+2)):
        print(i," ",i+2)

    