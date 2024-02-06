def farnheit_to_celcius(f):
    c=((f-32)*5)/9
    return c

try:
    farnheit=float(input("Enter the farhnei number: "))
    
    print("The celcius temperature: ",farnheit_to_celcius(farnheit))

except :
    print("Enter correct  number value: ")

