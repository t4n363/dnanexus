import array

# Check for requirement that min element of the array is less then x, and max element of the array is less or equal to x
def search_insert_position(arr, x):
    # Check if the array is empty
    if not arr:
        return -1

    # If j = 0, then requirment A[0], ..., A[j - 1] if out of range
    if x <= arr[0]:
        return -1

    # Check if x is greater than the maximum value in the array
    if x > arr[-1]:
        return -1

    # Initialize low and high indices for binary search
    low, high = 0, len(arr) - 1

    # Binary search algorithm, because input is sorted
    while low <= high:
        # Calculate mid index
        mid = (low + high) // 2

        # If the element at mid is less than x, search in the right half
        if arr[mid] < x:
            low = mid + 1
        # If the element at mid is greater than or equal to x, search in the left half
        elif arr[mid] >= x:
            high = mid - 1

    # The 'low' index represents the correct j position for x
    return low

# Example usage:
arr = array.array('i', [1, 4, 4, 4, 4, 4, 4, 4, 7])
x = 4
result = search_insert_position(arr, x)
assert result == 1,f"expected 1, got {result}"

arr = array.array('i', [1, 1, 3, 4, 5, 6, 7, 7, 7])
x = 1
result = search_insert_position(arr, x)
assert result == -1,f"expected -1, got {result}"

arr = array.array('i', [1, 1, 3, 4, 5, 6, 7, 7, 7])
x = 7
result = search_insert_position(arr, x)
assert result == 6,f"expected 6, got {result}"

arr = array.array('i', [1, 1, 3, 4, 5, 6, 7, 7, 7])
x = 8
result = search_insert_position(arr, x)
assert result == -1,f"expected -1, got {result}"

arr = array.array('i', [1, 1, 3, 4, 5, 6, 7, 7, 7])
x = 5
result = search_insert_position(arr, x)
assert result == 4, f"expected 4, got {result}"

