#To check if the pair with given sum exits in the array 
arr = list(map(int,input("Enter elements in the array with space between them: ").split()))
target = int(input("Enter sum: "))
arr.sort()
a = len(arr)
found = False
left = 0
right = a-1
while left<right :
        if arr[left]+ arr[right] > target:
            right -= 1
        elif arr[left] + arr[right] < target:
            left += 1
        elif arr[left]+arr[right] == target:
            found = True
            break
if found:
    print(f"The elements having {target} as their sum exist")
else:
    print(f"The elements having {target} as their sum doesnot exist")