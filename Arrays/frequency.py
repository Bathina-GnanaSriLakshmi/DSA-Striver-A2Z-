#To find the element that appears only once
arr = list(map(int,input("Enter elements: ").split(" ")))
dict1 = {}
for i in arr:
    if i in dict1:
        dict1[i] += 1
    else:
        dict1[i] = 1
for key,value in dict1.items():
    if value == 1:
        print(f"The element that appears only once is {key}")