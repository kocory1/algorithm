import numpy as np
import time
import matplotlib.pyplot as plt

def insertion_sort(arr):
    #to do
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -=1
        arr[j+1] = key
    return arr

def merge_sort(arr):
    #to do
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        
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
    return arr

sizes = [10, 100, 1000, 10000]

insertion_times = []
merge_times = []

for size in sizes:
    arr = np.random.randint(0, 10000, size)
    
    #insertion sort
    start_time = time.time()
    insertion_sort(arr)
    insertion_times.append(time.time() - start_time)
    
    #merge sort
    start_time = time.time()
    merge_sort(arr)
    merge_times.append(time.time() - start_time)

plt.figure()
plt.plot(sizes, insertion_times, marker='o', label='Insertion Sort')
plt.plot(sizes, merge_times, marker='^', label='Merge Sort')
plt.xlabel('Input Size (n)')
plt.ylabel('Runtime (s)')
plt.title('Empirical Runtime Comarison: Insertion vs Merge Sort')
plt.legend()
plt.grid(True)
plt.show()
