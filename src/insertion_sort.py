import numpy as np
import time

def insertion_sort_asc(arr):
    #to do
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -=1
        arr[j+1] = key
    return arr

def insertion_sort_desc(arr):
    #to do
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and arr[j] < key:
            arr[j+1] = arr[j]
            j -=1
        arr[j+1] = key
    return arr

def insertion_sort(arr, order):
    if order == "asc":
        return insertion_sort_asc(arr)
    elif order == "desc":
        return insertion_sort_desc(arr)
    else:
        return "Invalid order"

A = [5,2,7,6,0,8,3,4,9,1]
start_time = time.time()
A_asc = insertion_sort_asc(A)
end_time = time.time()
print(f"Time taken: {end_time - start_time} seconds")
print(A_asc)

start_time = time.time()
A_desc = insertion_sort_desc(A)
end_time = time.time()
print(f"Time taken: {end_time - start_time} seconds")
print(A_desc)

n = int(input("Enter the number of elements: "))
A = np.random.randint(0, 100, n)
print(insertion_sort(A, (input("Choose the order asc or desc:"))))