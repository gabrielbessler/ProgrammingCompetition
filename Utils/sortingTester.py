from sorting import quickSort, isSorted

L1 = [-5, -4, -2, 0, 1, 5, 19] 
L2 = reversed(L1) 
L3 = [-5, 10, 3, -5, 3, 2, 1, 1]

# Fully sorted list 
assert isSorted(quickSort(L1)) and len(quickSort(L1)) == len(L1)

# List that is sorted in reverse order 
assert isSorted(quickSort(L2)) and len(quickSort(L2)) == len(L2) 

# List that is not sorted 
assert isSorted(quickSort(L3)) and len(quickSort(L3)) == len(L3)

