def bubble(arr):
    """
    Sorts an array using the bubble sort algorithm.
    
    Parameters:
    arr (list): The list of elements to be sorted.

    Algorithm:
    1. Iterate through the list multiple times.
    2. Compare adjacent elements and swap them if they are in the wrong order.
    3. Repeat until no swaps are needed, indicating the list is sorted.
    4. Return the sorted list.
    
    Returns:
    list: The sorted list.

    Follow up:
    In every iteration, the maximum element bubbles up to its correct position i.e. the end of the list.
    if no swaps are made in an iteration, the list is already sorted.
    """
    n = len(arr)
    for i in range(n):
        # Track if a swap was made
        swapped = False
        for j in range(0, n-i-1):
            # Compare adjacent elements
            if arr[j] > arr[j+1]:
                # Swap if they are in the wrong order
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        # If no swaps were made, the array is sorted
        if not swapped:
            break
    return arr

# Example usage:
if __name__ == "__main__":  
    sample_array = [64, 34, 25, 12, 22, 11, 90]
    sorted_array = bubble(sample_array)
    print("Sorted array:", sorted_array)