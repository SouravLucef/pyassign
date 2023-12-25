

def lcm(a,b,c):
    c=c+b
    if(c%a==0 and c%b==0):
        return c
    return lcm(a,b,c)

n=int(input("Enter the first number :"))
m=int(input("Enter the second number :"))
c=0
print("LCM of ",n,"and",m,"is :",lcm(n,m,c))