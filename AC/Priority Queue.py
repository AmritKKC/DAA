import math
import random
from time import perf_counter_ns
import numpy as np
import matplotlib.pyplot as plt


def Heapify(arr, i):
    l = i * 2 + 1   # Left child of parent at index i.
    r = i * 2 + 2   # Right child of parent at index i.

    # Checking if left child is greater than parent and also index of left child less than array length.
    if l < len(arr) and arr[l] > arr[i]:
        largest = l
    else:
        largest = i
    # Checking if right child is greater than parent and also the index of right child less than array length.
    if r < len(arr) and arr[r] > arr[largest]:
        largest = r
    # If parent is not largest then exchange the value with largest child.
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        Heapify(arr, largest)   # Calling heapify to make heap again.


def Max_Heap(arr):
    heapsize = len(arr) # Array length.
    for i in range(heapsize // 2 - 1, -1, -1):  # Running for loop from last parent to the root node.
        Heapify(arr, i)


def Maximum(arr):
    return arr[0]   # Return root element which is maximum in heap.


def Extract_Max(arr):
    heapsize = len(arr) # Array length.
    if heapsize < 0:
        print("Error: Heap Underflow")
    max = arr[0]    # Extracting root element.
    arr[0] = arr[heapsize - 1]  # Moving last leaf node element to root.
    arr.pop()   # Removing last leaf node from heap.
    Heapify(arr, 0) # Calling heapify to make heap again.
    return max  # Returning maximum element.


def Increase_Key(arr, i, key):
    # Checking if key is smaller than the element at index before inceasing.
    if key < arr[i]:
        print("Error: New key is smaller than current key.")
    arr[i] = key    # Changing element if key is greater.
    # Now comaparing and changing with its children to make it heap again.
    while i > 0 and arr[(i - 1) // 2] < arr[i]:
        arr[i], arr[(i - 1) // 2] = arr[(i - 1) // 2], arr[i]
        i = (i - 1) // 2


def Insert(arr, key):
    arr.append(-1)  # Adding any negative value in array to increase size of array.
    Increase_Key(arr, len(arr) - 1, key)    # Calling increase key to insert the key.


# Arrays for storing values.
t_maximum = []
t_extractmax = []
t_increasekey = []
t_insert = []
x = []
logn = []
for loop in range(1, 11):
    size = loop * 24000  # Length of input array.
    x.append(size)
    logn.append((math.log2(size))*500)   # Logn

    # Creating arraay to perform heap operations.
    arr = [random.randint(100, 900) for i in range(size)]

    # Calling Max Heap function to make a max heap of given array.
    Max_Heap(arr)

    # Maximum function to return maximum element of heap.
    start = perf_counter_ns()
    Maximum(arr)
    end = perf_counter_ns()
    total = end - start
    t_maximum.append(total)

    # Extract_Max function to extract the maximum element from the heap.
    start = perf_counter_ns()
    Extract_Max(arr)
    end = perf_counter_ns()
    total = end - start
    t_extractmax.append(total)

    # Increase_Key function to increase key value at given index.
    start = perf_counter_ns()
    Increase_Key(arr, random.randint(100, 900), random.randint(900, 1500))  # Increase_Key(Array, Index, Key)
    end = perf_counter_ns()
    total = end - start
    t_increasekey.append(total)

    # Insert Function to insert a element in heap.
    start = perf_counter_ns()
    Insert(arr, random.randint(100, 900))   # Insert(Array, Key)
    end = perf_counter_ns()
    total = end - start
    t_insert.append(total)

# Plotting values on graph.
plt.title("Heap Operations Time Complexity")
plt.xlabel("Array Size (n)")
plt.ylabel("Time")
plt.plot(x, logn, label="logn")
plt.plot(x, t_maximum, label="Maximum")
plt.plot(x, t_extractmax, label="Extract_Max")
plt.plot(x, t_increasekey, label="Increase_Key")
plt.plot(x, t_insert, label="Insert")
plt.legend()
plt.show()
