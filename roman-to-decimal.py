roman_code	= {
"I": 1,
"V": 5,
"X": 10,
"L": 50,
"C": 100,
"D": 500,
"M": 1000
}

s = input("Enter the roman number: ")
n = len(s)

num : int = roman_code[s[n-1]]

for i in range(n-2,-1,-1):
	if roman_code[s[i]] >= roman_code[s[i+1]]:
		num += roman_code[s[i]]
	else :
		num -= roman_code[s[i]]
	
print(num)