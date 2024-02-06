def fact_while_loop(num):
    fact=1
    while num>0:
        fact=fact*num
        num-=1
    return fact

try:
    numb=int(input("Enter a number : "))
    if(numb>=0):
        print(f"Factorial of {numb} is : {fact_while_loop(numb)}")
    else:
        print("Enter a positive number!!!")
except:
    print("Please enter a number !!")