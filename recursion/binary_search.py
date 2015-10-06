def binary_search(arr,low,high,number):
	mid = (low + high) / 2
	if (arr[mid] == number):
		return arr[mid]
	elif (arr[mid] > number):
		return binary_search(arr,low,mid - 1,number)
	else:
		return binary_search(arr,mid + 1, high,number)

arr = [1,2,3,4,5,6] 
low = 0
high = (len(arr) - 1)
print binary_search(arr,low,high,5)

