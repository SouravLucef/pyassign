#Program to find factorial using while loop

num=int(input("Enter the number :"))
fact=1
if(num == 0):
    print("Factorial of ",num,"is ",1)
elif(num<0):
    print("Enter a Positive Number")
else:
    i=1
    while(i<=num):
        fact=fact*i
        i=i+1
    print("Factorial of",num," is :",fact)