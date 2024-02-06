def prime(num):
    if num>1:
        for i in range (2,(num//2)+1):
            if (num % i==0):
                print("the number is not a prime numnber:")
                break
        else:
            print("The number is a prime number..")
    else:
        print("The number is not a prime number..")

try:
    number=int(input("Enter a number :"))
    prime(number)
except Exception as e:
    print(e)
    print("Please try again !!!!!")