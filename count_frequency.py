def freqCountUsingDict(arr):
	freq = {}
	for i in arr:
		if i not in freq:
			freq[i] = 0
		freq[i] += 1
	print(freq)

arr = [ 1,2,1,90,23,3214,53,34,662,1,2,90,23,50]
freqCountUsingDict(arr)

