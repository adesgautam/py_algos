
# Adesh Gautam

def merge(arr, l, m, r):

    L = arr[:m]
    R = arr[m:]
    n1 = len(L)
    n2 = len(R)
 
    i, j, k = 0, 0, 0    
 
    while i < n1 and j < n2 :
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
 
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def mergeSort(arr,l,r):
    if l < r:
        # Same as (l+r)/2, but avoids overflow for
        # large l and h
        m = (l+(r-1))/2
 
        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)
 
arr = [12, 11, 13, 5, 6, 7]
n = len(arr)
print("Given array is: {0}".format(arr))
 
mergeSort(arr,0,n)
print("Sorted array is: {0}".format(arr))

