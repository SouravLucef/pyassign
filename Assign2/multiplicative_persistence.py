# #Yes, you've described the concept of multiplicative digital roots and multiplicative persistence. Let me provide a simple example to illustrate these concepts:

# Let's take the number 679.

# Multiplicative Digital Root:

# 6×7×9=378
# 3×7×8=168
# 1×6×8=48
# 4×8=32
# 3×2=6
# So, the multiplicative digital root of 679 is 6.

# Multiplicative Persistence:
# In this case, it took 4 steps to reduce the number to a single digit. Therefore, the multiplicative persistence of 679 is 4.
# The goal is to find the multiplicative digital root and the multiplicative persistence for a given number by repeating the process of multiplying its digits until a single-digit result is obtained and counting the number of steps it takes.

# These concepts are often used as interesting mathematical puzzles and can vary for different numbers. Some numbers have higher multiplicative persistence than others, and finding the persistence for large numbers can be a challenging problem.


def multi_digital_root_and_persistence(n):
    persistence = 0
    while n >= 10:
        num=n
        r = 1
        while(num>0):
            rem=num%10
            r =r*rem
            num =num//10
        persistence += 1
        n=r
    return n, persistence

# Example usage:
n=int(input("Enter a number :"))
digital_root, persistence = multi_digital_root_and_persistence(n)

print("Multiplicative Digital Root of ",n,": ",digital_root)
print("Multiplicative Persistence of ",n,":", persistence)




