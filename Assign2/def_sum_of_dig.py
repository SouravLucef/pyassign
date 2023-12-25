def sum_of_digit( n ):
	if n == 0:
		return 0
	return (n % 10 + sum_of_digit(n // 10))


n = int(input("Enter the number whose sum of digits you want:"))

print("Sum of digits of number",n,"is", sum_of_digit(n))