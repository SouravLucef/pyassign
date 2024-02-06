#program to check for the armstrong number..
#153=(1)^3 + (5)^3 + (3)^3 , 1634=(1)^4+(6)^4+(3)^4+(4)^4

def check_armstrog(num):
    l=len(str(num))
    t_num=0
    while num > 0:
        rem=num%10
        t_num=t_num+rem**l
        num=num//10
    return t_num

numb=int(input("Enter a number : "))
numb2=check_armstrog(numb)
if(numb2==numb):
    print("The number is a armstrong number")
else:
    print("The number is not a armstrong number")
