def selection_sort(arr):
    """
    Sorts an array using the selection sort algorithm.
    
    Parameters:
    arr (list): The list of elements to be sorted.

    Algorithm:
    1. Iterate through the list.
    2. For each position, find the smallest element in the unsorted portion of the list.
    3. Swap the smallest element with the element at the current position.
    
    Returns:
    list: The sorted list.
    """
    n = len(arr)
    for i in range(n):
        # Assume the minimum is the first element
        min_index = i
        for j in range(i + 1, n):
            # Update min_index if the current element is smaller
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# Example usage:
if __name__ == "__main__":  
    sample_array = [64, 25, 12, 22, 11, 55, 7]
    sorted_array = selection_sort(sample_array)
    print("Sorted array:", sorted_array)