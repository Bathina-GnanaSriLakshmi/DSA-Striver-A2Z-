#To find the Majority Element that occurs more than N/2 times
def majority_element(arr):
    count = 0
    element = None
    for num in arr:
        if count == 0:
            element = num
        if num == element:
            count += 1
        else:
            count -= 1
    return element
arr = list(map(int,input("Enter elements with space:")))
print(majority_element(arr))