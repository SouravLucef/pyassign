#Write a recursive function that will calculate a to the power b

def pow(a,b):
    if(b==0):
        return 1
    return a*pow(a,b-1)

a=int(input("Enter the number: "))
b=int(input("Enter the power :"))

print(pow(a,b))