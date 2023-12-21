#Program to show the multiplication table of a number

def multi(n):
    for i in range(1,11):
        print(n,"X",i,"=",n*i)


n=int(input("Enter the number: "))
multi(n)