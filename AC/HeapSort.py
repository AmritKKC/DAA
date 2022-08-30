import time
import numpy as np
import matplotlib.pyplot as plt
import math


def heapify(arr, n, i):
    l = 2 * i + 1  # index value of left child.
    r = 2 * i + 2  # index value of right child.
    # To check if left child of root exists and is greater than root.
    if l < n and arr[l] > arr[i]:
        largest = l
    else:
        largest = i
    # To check if right child of root exists and is greater than root.
    if r < n and arr[r] > arr[largest]:
        largest = r
    if largest != i:    # Changing parent with child when child is greater than parent.
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)    # Using recursion to make array again heap.


# Function to build heap of an array.
def BuildHeap(arr):
    n = len(arr)  # Array length.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)  # Calling heapify to make array a heap.


# Function to perform heap sort.
def heapSort(arr):
    n = len(arr)
    BuildHeap(arr)  # Calling function to build heap of given array.
    # One by one extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)


# Driver code
num = []
tm = []
y = []
for i in range(1, 21):
    size = i * 1
    arr = np.random.randint(1, 2000, size)
    n = len(arr)
    num.append(n)
    print("\n\nGiven array is: ")
    for i in range(n):
        print("%d" % arr[i], end=" ")
    start = time.time()
    heapSort(arr)
    end = time.time()
    print("\n\nSorted array is: ")
    for j in range(n):
        print("%d" % arr[j], end=" ")
    tm.append((end - start))
    y.append((n * math.log2(n)))
    print("\n\n--- ", end - start, " nano seconds ---")
plt.title("Heap Sort Time Complexity")
plt.xlabel("Array Size (n)")
plt.ylabel("Time")
plt.plot(num, tm, label="Heap Sort")
plt.plot(num, y, label="nLogn")
plt.legend()
plt.show()
