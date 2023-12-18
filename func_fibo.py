#Program to print the fibonacci series using functin:
def fibo(n):
    if(n<=1):
        return n
    else:
        return fibo(n-1)+fibo(n-2)


n=int(input("Enter the number of terms :"))

if(n<0):
    print("-: Enter a positive number :-")
else:
    for i in range(n):
        print(fibo(i))
