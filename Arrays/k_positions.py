#To rotate the array by k positions
k = int(input("Enter the value of k: "))
arr = list(map(int,input("Enter elements in array: ").split(" ")))
l = len(arr)
left = 0
right = l-1
while(left < right):
    temp = arr[left]
    arr[left] = arr[right]
    arr[right] = temp
    left +=1
    right-= 1
left = 0
right = k-1
while(left < right):
    temp = arr[left]
    arr[left] = arr[right]
    arr[right] = temp
    left +=1
    right-= 1
left = k
right = l-1
while(left < right):
    temp = arr[left]
    arr[left] = arr[right]
    arr[right] = temp
    left +=1
    right-= 1
print(arr)