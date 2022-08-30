# Write a program to implement Merge Sort algorithm.
# Plot the graph of the time complexity for different values of array size ‘n’.
# Compare this with the plot of n^2.
import time
import random
import matplotlib.pyplot as plt


def merge(a, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    # create temp arrays
    left = [0] * n1
    right = [0] * n2

    # Copy data to temp arrays left[] and right[]
    for i in range(0, n1):
        left[i] = a[l + i]

    for j in range(0, n2):
        right[j] = a[m + 1 + j]

    # Merge the temp arrays back into a[l..r]
    i = 0  # Initial index of first sub array
    j = 0  # Initial index of second sub array
    k = l  # Initial index of merged sub array

    while i < n1 and j < n2:
        if left[i] <= right[j]:
            a[k] = left[i]
            i += 1
        else:
            a[k] = right[j]
            j += 1
        k += 1

    # Copy the remaining elements of left[], if there are any
    while i < n1:
        a[k] = left[i]
        i += 1
        k += 1

    # Copy the remaining elements of right[], if there are any
    while j < n2:
        a[k] = right[j]
        j += 1
        k += 1


def mergesort(a, l, r):
    if l < r:
        m = l + (r - l) // 2
        mergesort(a, l, m)
        mergesort(a, m + 1, r)
        merge(a, l, m, r)


xaxis = list()
yaxis = list()
n2 = list()
for x in range(1, 11):
    start_time = time.time_ns()
    inputsize = x * 12000
    xaxis.append(inputsize)
    a = [random.randint(100, 500) for i in range(inputsize)]
    n = len(a)
    print("Given array is")
    for i in range(n):
        print("%d" % a[i], end=" ")
    mergesort(a, 0, n - 1)
    print("\n\nSorted array is")
    for i in range(n):
        print("%d" % a[i], end=" ")
    yaxis.append(time.time_ns() - start_time)
    n2.append(inputsize ** 2)
    print("\n\n--- %s nano seconds ---" % (time.time_ns() - start_time))

plt.plot(xaxis, yaxis, label="Merge Sort")
plt.plot(xaxis, n2, label="n^2")
plt.yscale('linear')
plt.xlabel('Input Size (N)')
plt.ylabel('Time')
plt.title("Time Complexity Graph\nMerge Sort V/s n^2")
plt.legend()
plt.show()
