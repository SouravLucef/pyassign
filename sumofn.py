#program to find the sum of first n natural numbers
n=int(input("Enter the term : "))
sum=0
if(n<0):
    print("Enter a positive number..")
else:
    for i in range(1,n+1):
        sum=sum+i
    print("Sum o first ",n,"natural numbers is : ",sum)