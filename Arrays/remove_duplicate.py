#To remove duplicate in-place from sorted array
def remove_duplicates(arr):
    n = len(arr)
    if n == 0 or n == 1:
        return n
    write_index = 0  
    for read_index in range(1, n):
        if arr[read_index] != arr[write_index]:
            write_index += 1
            arr[write_index] = arr[read_index]
    return write_index + 1
arr = list(map(int, input("Enter sorted elements: ").split()))
k = remove_duplicates(arr)
print("Number of unique elements:", k)
print("Array after removing duplicates:", arr[:k])