def insertion_sort(arr):
    """
    Perform insertion sort on the given list.

    :param arr: List of elements to be sorted
    :return: Sorted list
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    
    return arr


# Example usage:
if __name__ == "__main__":
    sample_array = [12, 11, 13, 5, 6]
    sorted_array = insertion_sort(sample_array) 
    print("Sorted array:", sorted_array)
