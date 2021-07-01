def factorial(num: int):
	fact = 1
	for j in range(1,num+1):
				fact *= j
	return fact

# if __name__ == "__main__":

number1 = int(input("enter the first number: "))
number2 = int(input("enter the second number: "))

for n in range(number1, number2+1) :
	print(factorial(n))	