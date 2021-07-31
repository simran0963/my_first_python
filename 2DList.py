arr = [ [0,1,2] , [3,4,5] , [6,7,8] ]

r  = len(arr)
c  =  len(arr[0])

for i in range(r):
	for j in range(c):
		print(arr[i][j],end=' ')
	print()