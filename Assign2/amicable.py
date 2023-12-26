n=int(input("Enter the 1st number :"))
m=int(input("Enter the 2nd number :"))
s1,s2=0,0
for i in range(1,n):
    if(n%i==0):
        s1 +=i
for i in range(1,m):
    if(m%i==0):
        s2+=i

if(s1==m and s2==n):
    print("The two",n,"and",m," numbers  are Amicable number")
else:
    print("The two",n,"and",m," numbers are not Amicable numbers")