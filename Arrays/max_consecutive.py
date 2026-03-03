#To Count Maximum Consecutive One's in the array
def find_max_consecutive_ones(nums):
    cnt = 0 
    maxi = 0 
    for i in range(len(nums)):
        if nums[i] == 1:
            cnt += 1
            maxi = max(maxi, cnt)
        else:
            cnt = 0
    return maxi
nums = list(map(int, input("Enter binary elements (0/1): ").split()))
print("Maximum consecutive 1's:", find_max_consecutive_ones(nums))