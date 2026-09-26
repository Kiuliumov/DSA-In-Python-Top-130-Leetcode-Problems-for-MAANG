def merge(left, right):
    n = len(left) + len(right)
    i = 0
    j = 0
    merged = [0] * n
    for curr in range(n):
        if i == len(left):
            merged[curr] = right[j]
            j += 1
        elif j == len(right):
            merged[curr] = left[i]
            i += 1
        else:
            if left[i] < right[j]:
                merged[curr] = left[i]
                i += 1
            else:
                merged[curr] = right[j]
                j += 1
    return merged

def mergeSort(array):
    if len(array) == 1:
        return array
    
    mid = len(array) // 2
    left = mergeSort(array[:mid])
    right = mergeSort(array[mid:])
    
    return merge(left, right)

arr = mergeSort([5, 6, 5, 6, 5, 6])

print(arr)