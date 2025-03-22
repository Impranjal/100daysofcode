def peak_element(arr):
    n = len(arr)
    
    # Edge case: If the array has only one element, it is a peak
    if n == 1:
        return True
    
    # Iterate through the array
    for i in range(n):
        # Check if current element is greater than neighbors
        if (i == 0 or arr[i] > arr[i - 1]) and (i == n - 1 or arr[i] > arr[i + 1]):
            return True  # A peak exists

    return False  # No peak found
arr = [1, 2, 4, 5, 7, 8, 3]
print(peak_element(arr))