import time
import random
from matplotlib import pyplot as plt


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]    # Taking element from array for comparison.
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j] # Replacing if key is less than index value.
            j = j-1
        arr[j + 1] = key
    return arr


def bucket_sort(arr):
    B = []  # Creating empty array.
    for i in range(10):
        B.append([])    # Adding empty array in B as a bucket.
    for j in arr:
        index = int(10*j)
        B[index].append(j)  # Inserting values in bucket.
    for i in range(10):
        B[i] = insertion_sort(B[i]) # Calling insertion sort to sort the bucket.
    k = 0
    for x in range(10):
        for y in range(len(B[x])):
            arr[k] = B[x][y]    # Adding elements from bucket in a array after sorting.
            k += 1
    return arr


x = [] 
t = []
for loop in range(1, 11):
    size = loop * 200    # Array size.
    A = [random.uniform(0.001, 0.999) for i in range(size)]
    x.append(size)
    print(f'\nGiven array: {A}')
    start = time.time_ns()
    bucket_sort(A)  # Calling bucket sort function.
    t.append((time.time_ns() - start)/10**4)
    print(f'\nSorted array: {A}')
# Plotting graph
plt.title("Time Complexity Graph\nBucket Sort V/s O(n)")
plt.xlabel('Input Length (N)')
plt.ylabel('Time (in nano seconds)')
plt.plot(x, x, label='O(n)')
plt.plot(x, t, label='Bucket Sort')
plt.legend()
plt.show()