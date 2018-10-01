

def quickSort(L, method): 
    ''' 
    O(nlogn) in average case
    O(n^2) worst case   
    In place sorting algorithm. In practice, the worst case is usually avoided. 

    1. Partition: Pick a pivot and rearrange so that all the elements smaller 
        than the pivot are to the left of it and all elements greater than it 
        are to the right. 
    2. Then, we run quickSort() on the left sub-array (to the left of the pivot) 
        and the right sub-array

    Methods for picking the pivot: 
    1. Always pick the last element 
    2. Always pick the first element 
    3. Pick a random element 
    4. Pick the median element 

    We use (start, end) for the recursive calls to quickSort so we can do sorting in place.
    ''' 
    quickSortHelper(L, 0, len(L) - 1, method)

def quickSortHelper(L, startIndex, endIndex, method): 
    # If startIndex >= endIndex, the list must be sorted (this is our base case) 
    # This also prevents issues with passing in (pivotIndex - 1) when pivotIndex = 0
    if (startIndex < endIndex):
        pivotIndex = partition(L, startIndex, endIndex)
        quickSortHelper(L, startIndex, pivotIndex-1)
        quickSortHelper(L, pivotIndex + 1, endIndex)
    
def partition(L, startIndex, endIndex): 
    ''' 
    Returns the index of the pivot after list has been rearranged
    '''
    return 0 

def isSorted(L): 
    ''' 
    Returns true if the input list L is sorted 
    ''' 
    return all(L[i] <= L[i + 1] for i in range(len(L) - 1))