#Program to reverse a number
num=int(input("Enter the number :"))
sum=0
n=num
while(num>0):
    rem=num%10
    sum=sum+rem
    num=num//10

print("Sum of digits : " ,sum)