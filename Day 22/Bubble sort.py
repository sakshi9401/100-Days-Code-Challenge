def bubbleSort(arr):
	
	n = len(arr)
	
	for i in range(n):
		for j in range(0, n - i - 1):
		
			if arr[j] > arr[j + 1]:
				arr[j], arr[j + 1] = arr[j + 1], arr[j]
				
arr = []

n = int(input("Enter number of elements : "))

for i in range(0, n):
    ele = int(input())
  
    arr.append(ele)

bubbleSort(arr)

print("Sorted array is:")
for i in range(len(arr)):
	print("%d" % arr[i])

