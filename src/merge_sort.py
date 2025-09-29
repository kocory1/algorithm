import numpy as np

def merge_sort(arr):
    #to do
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        merge(arr, L, R)
    return arr

def merge(arr, L, R):
        i = 0
        j = 0
        k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1
        while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1    
    

arr = [5,2,7,6,0,8,3,4,9,1]
print(merge_sort(arr))

arr = np.random.randint(0, 10000, 10)
print(merge_sort(arr))

arr = np.random.randint(0, 10000, 100)
print(merge_sort(arr))

arr = np.random.randint(0, 10000, 1000)
print(merge_sort(arr))

arr = np.random.randint(0, 10000, 10000)
print(merge_sort(arr))