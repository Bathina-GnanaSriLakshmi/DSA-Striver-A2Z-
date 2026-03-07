#To find the  maximum subarray sum in the array
def max_sum(arr):
    max = arr[0]
    sum = 0
    sub_array = []
    best_subarray = []
    n = len(arr)
    for i in range(0,n):
        sum += arr[i]
        sub_array.append(arr[i])
        if sum> max:
            max = sum
            best_subarray = sub_array.copy()
        if sum<0:
            sum = 0
            sub_array = []
    print(f"The maximum subarray sum is {max}")
    print(f"The subarray is {best_subarray}")
arr = list(map(int,input("Enter elements with space between them: ").split( )))
max_sum(arr)  