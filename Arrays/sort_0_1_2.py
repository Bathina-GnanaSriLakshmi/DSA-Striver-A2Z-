#To sort an array consisting only 0's , 1's , 2's 
def sort_array(arr):
    low = 0
    mid = 0
    high = len(arr) - 1
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:  
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    return arr
arr = list(map(int,input("Enter elements with space: ").split()))
print(sort_array(arr))