import random

def my_quicksort_v1(arr):
    """
    Sorts a list in ascending order using the quicksort algorithm with 2-way partition.

    Parameters:
    - arr (list): The list to be sorted.

    Returns:
    - list: A new list containing the sorted elements.
    """
    def _my_quicksort(arr, start, stop):
        """
        Recursively performs the quicksort algorithm on a sublist.

        Parameters:
        - arr (list): The list to be sorted.
        - start (int): The starting index of the sublist.
        - stop (int): The stopping index (exclusive) of the sublist.
        """
        if stop - start < 2:
            return

        # Randomly choose a pivot element
        idx = random.randint(start, stop - 1)
        arr[idx], arr[stop - 1] = arr[stop - 1], arr[idx]
        idx = my_partition(arr, start, stop)

        _my_quicksort(arr, start, idx)
        _my_quicksort(arr, idx + 1, stop)

    def my_partition(arr, start, stop):
        """
        Performs the 2-way partition for the quicksort algorithm.

        Parameters:
        - arr (list): The list to be partitioned.
        - start (int): The starting index of the partition range.
        - stop (int): The stopping index (exclusive) of the partition range.

        Returns:
        - int: The final position of the pivot element after partitioning.
        """
        i = start
        j = stop - 2
        pivot = arr[stop - 1]

        while i <= j:
            if arr[i] <= pivot:
                i += 1
            elif arr[j] >= pivot:
                j -= 1
            else:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1

        arr[i], arr[stop - 1] = arr[stop - 1], arr[i]
        return i

    arr_copy = arr.copy()  # Create a copy of the input list
    _my_quicksort(arr_copy, 0, len(arr_copy))
    return arr_copy


def my_quicksort_v2(arr):
    """
    Sorts a list in ascending order using the quicksort algorithm with 3-way partition.

    Parameters:
    - arr (list): The list to be sorted.

    Returns:
    - list: A new list containing the sorted elements.
    """
    def _my_quicksort(arr, start, stop):
        """
        Recursively performs the quicksort algorithm on a sublist.

        Parameters:
        - arr (list): The list to be sorted.
        - start (int): The starting index of the sublist.
        - stop (int): The stopping index (exclusive) of the sublist.
        """
        if stop - start < 2:
            return

        # Randomly choose a pivot element
        pivot = arr[random.randint(start, stop - 1)]
        idx_1 = idx_2 = start
        idx_3 = stop

        while idx_2 < idx_3:
            if arr[idx_2] < pivot:
                arr[idx_2], arr[idx_1] = arr[idx_1], arr[idx_2]
                idx_1 += 1
                idx_2 += 1
            elif arr[idx_2] == pivot:
                idx_2 += 1
            else:
                idx_3 -= 1
                arr[idx_2], arr[idx_3] = arr[idx_3], arr[idx_2]

        _my_quicksort(arr, start, idx_1)
        _my_quicksort(arr, idx_3, stop)

    arr_copy = arr.copy()  # Create a copy of the input list
    _my_quicksort(arr_copy, 0, len(arr_copy))
    return arr_copy
