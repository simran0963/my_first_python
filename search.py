li = list(map(int,input("enter the list elements separated by spaces in a non decreasing order: ").split())) # to enter a list
key = int(input("enter the key : "))
# print('List is ' , li)
# print('Key is ', key)

# print(key in li) 

def linearSearch(li,key)->bool:
	for i in li:
		if i == key:
			return True
	return False


def binarySearch(li,key)->bool:
	low , high = 0 , len(li)-1
	while(low <= high):
		mid = ( low + high ) // 2
		if li[mid] == key:
			return True
		elif li[mid] > key:
			high = mid - 1
		else:
			low = mid + 1
	return False
