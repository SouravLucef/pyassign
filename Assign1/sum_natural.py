#program to print the sum of first n natural numbers

def sum_of_numb(num):
    sum=0
    for i in range(1,num+1):
        sum+=i
    return sum

try:
    numb=int(input("Enter a number : "))
    if(numb > 0):
        print(f"Sum of {numb} natural number is : {sum_of_numb(numb)}")
    else:
        raise Exception("Number should b greater than zero")
except Exception as e:
    print(e)