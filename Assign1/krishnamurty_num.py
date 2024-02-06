#program to check for krishnamurty number.
#145=1!+4!+5!

def fact(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact

def krishnamurty_num(num):
    t_num=0
    while num>0:
        rem=num%10
        t_num+=fact(rem)
        num=num//10
    print(t_num)
    return t_num

numb=int(input("Enter a number : "))
if(krishnamurty_num(numb) == numb):
    print("THe number is a krishnamurty number ")
else:
    print("The number is not a krishnamurty number.")