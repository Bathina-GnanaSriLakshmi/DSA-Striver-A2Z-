# To find the union of two sorted arrays
def union_sorted_arrays(arr1, arr2):
    i, j = 0, 0
    n1, n2 = len(arr1), len(arr2)
    result = []
    while i < n1 and j < n2:
        if arr1[i] < arr2[j]:
            if not result or result[-1] != arr1[i]:
                result.append(arr1[i])
            i += 1
        elif arr1[i] > arr2[j]:
            if not result or result[-1] != arr2[j]:
                result.append(arr2[j])
            j += 1
        else:
            if not result or result[-1] != arr1[i]:
                result.append(arr1[i])
            i += 1
            j += 1
    while i < n1:
        if not result or result[-1] != arr1[i]:
            result.append(arr1[i])
        i += 1
    while j < n2:
        if not result or result[-1] != arr2[j]:
            result.append(arr2[j])
        j += 1

    return result
arr1 = list(map(int, input("Enter sorted elements of array 1: ").split()))
arr2 = list(map(int, input("Enter sorted elements of array 2: ").split()))
print("Union:", union_sorted_arrays(arr1, arr2))