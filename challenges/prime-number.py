def prime_check(num: int) -> bool:
	if num == 0 or num == 1:
		return False
	for i in range(2, num):
		if num % i == 0:
			return False
	else:
		return True

number1 = int(input("enter the first number: "))
number2 = int(input("enter the second number: "))

for j in range(number1, number2):
	if prime_check(j):
		print(j) 

# print(prime_check(9))