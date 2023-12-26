# Write a recursive function that will check a number is palindrome or not.
def rev_num(n, rev):
    if n == 0:
        return rev
    rem = n % 10
    rev = rev * 10 + rem
    return rev_num(n // 10, rev)

n = int(input("Enter the number: "))
rn = rev_num(n, 0)  # Initialize rev to 0
print(rn)

if n == rn:
    print("The number",n," is a palindrome.")
else:
    print("The number",n," is not a palindrome.")
