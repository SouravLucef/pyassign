#program to find palindrom number

def rev_num(num):
    rev_num=0
    while num >0:
        rem = num%10
        rev_num=rev_num*10+rem
        num = num//10
    return rev_num


numb = int(input("Enter a number : "))
if(rev_num(numb)== numb):
    print(f"The number {numb} is Palindrom .")
else:
    print(f"The  number {numb} is not a palindrom naumber.")