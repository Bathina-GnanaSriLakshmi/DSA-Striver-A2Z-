#To move zeros to end
arr = list(map(int, input("Enter elements in the array: ").split()))
j = 0 
for i in range(len(arr)):
    if arr[i] != 0:
        arr[i], arr[j] = arr[j], arr[i]
        j += 1
print(arr)