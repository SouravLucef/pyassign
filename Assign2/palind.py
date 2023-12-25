# Write a recursive function that will check a number is palindrome or not.

def rev_num(n):
    sum=0
    if(n<=0):
        return sum*10+0
    return (sum*10+n%10)+rev_num(n//10)

n=int(input("Enter the number :"))
rn=rev_num(n)
print(rn)
if(n==rn):
    print("The number is a palindrom number ..")