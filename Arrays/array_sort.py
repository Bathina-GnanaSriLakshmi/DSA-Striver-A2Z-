#To check whether the array is sorted or not
def is_sorted(arr):
    n = len(arr)
    if n == 0 or n == 1:
        print("Can't be determined")
    for i in range(1, n):
        if arr[i - 1] > arr[i]:
            return False
        else :
            return True

arr = list(map(int, input("Enter elements separated by space: ").split()))
print(is_sorted(arr))