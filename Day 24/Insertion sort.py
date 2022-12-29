def insertion_sort(arr):  
    for i in range(1, len(arr)):  
  
        value = arr[i]  
  
        j = i - 1  
        while j >= 0 and value < arr[j]:  
            arr[j + 1] = arr[j]  
            j -= 1  
            arr[j + 1] = value  
    return arr  
            
try:
    arr = []
      
    while True:
        arr.append(int(input()))

except:
    print("The unsorted list is:", arr)  
  
    print("The sorted list1 is:", insertion_sort(arr)) 
