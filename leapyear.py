#Program to check for leap year

y=int(input("Enter your year :"))
if(y%4==0 and (y%100!=0 or y%400==0)):
    print("Year",y,"is a Leap Year")
else:
    print("Year",y,"is not a leap Year")