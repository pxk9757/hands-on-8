def quickSelect(arr, low, high, i):
    if low == high:
        return arr[low]

    pivotIndex = partition(arr, low, high)

    if i == pivotIndex:
        return arr[i]
    elif i < pivotIndex:
        return quickSelect(arr, low, pivotIndex - 1, i)
    else:
        return quickSelect(arr, pivotIndex + 1, high, i)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Example usage:
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
ithElement = quickSelect(arr, 0, n - 1, 3)
print("The 3rd order statistic is:", ithElement)