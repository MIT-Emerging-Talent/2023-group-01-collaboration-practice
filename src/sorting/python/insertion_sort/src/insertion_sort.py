def insertion_sort(un_sorted_array):
    '''
    This function sorts the array based on insertion sort algorithm
    args:
        un_sorted_array: the array that we want to sort
    returns the same array but sorted
    '''
    for i in range(len(un_sorted_array)):
        current = i
        for j in range(i-1, -1, -1):
            if un_sorted_array[current] < un_sorted_array[j]:
                un_sorted_array[current], un_sorted_array[j] = un_sorted_array[j], un_sorted_array[current]
                current = j
            j -= 1
    return un_sorted_array

