#To reverse an array using two pointer technique 
arr = input("Enter elements: ").split()
l = len(arr)
left = 0
right = l-1
temp = 0
while(left<right):
    temp = arr[left]
    arr[left] = arr[right]
    arr[right] = temp
    left += 1
    right -= 1
print(arr)