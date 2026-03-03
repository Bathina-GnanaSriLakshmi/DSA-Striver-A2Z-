#To find the length of Longest Subarray with given Sum K(Positives)
def longest_subarray_with_sum_k(arr, k):
    left = 0
    current_sum = 0
    max_length = 0
    for right in range(len(arr)):
        current_sum += arr[right]
        while current_sum > k and left <= right:
            current_sum -= arr[left]
            left += 1
        if current_sum == k:
            max_length = max(max_length, right - left + 1)
    return max_length
arr = list(map(int, input("Enter array elements: ").split()))
k = int(input("Enter value of k: "))
print("Length of longest subarray with sum =", k, "is:",longest_subarray_with_sum_k(arr, k))