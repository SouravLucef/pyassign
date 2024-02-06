#Program to print the fibonacci series

def fibo(n):
    if (n==0) or (n==1):
        return n
    else:
        return fibo(n-2)+fibo(n-1)

try:
    num=int(input("Enter the number of terms : "))
    for i in range(num):
        print(fibo(i),end=" ")
except Exception as e:
    print(e)