arr = list(map(int,input("Enter array elements: ").split(" ")))
high = 0
second_high = 0
for i in arr:
    if i > high :
        second_high = high
        high = i
    elif i < high and i>second_high:
        second_high = i
print(f"The second highest number is {second_high}")   