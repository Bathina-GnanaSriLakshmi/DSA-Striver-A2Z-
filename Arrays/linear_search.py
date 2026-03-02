arr = input("Enter array elements: ").lower().split()
target = input("Enter the element to search:").lower()
index = 0
p = 0
for i in arr:
    if i == target:
        p = 1
        print(f"The element is at {index}")
    index += 1
if p==0:
    print("Element not found in the array")