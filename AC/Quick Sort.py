import time
import random
import matplotlib.pyplot as plt
import math


def partition(A, p, r):
    pivot = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= pivot:
            i = i + 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def quick_sort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q - 1)
        quick_sort(A, q + 1, r)


xaxis = []
yaxis = []
nlogn = []
for x in range(1, 11):
    inputsize = x * 20000
    xaxis.append(inputsize)
    A = [random.randint(100, 500) for i in range(inputsize)]
    print(f'\n\nGiven array: {A}')
    start_time = time.time_ns()
    quick_sort(A, 0, len(A) - 1)
    end_time = time.time_ns()
    yaxis.append(end_time - start_time)
    nlogn.append((inputsize * math.log2(inputsize))*4500)
    print(f'\nSorted array: {A}')
    print(f'\nTime Taken: {end_time - start_time}')
plt.plot(xaxis, yaxis, label="Quick Sort")
plt.plot(xaxis, nlogn, label="nLogn")
plt.xlabel('Input Size (N)')
plt.ylabel('Time')
plt.title("Time Complexity Graph\nQuick Sort V/s nLogn")
plt.legend()
plt.show()
