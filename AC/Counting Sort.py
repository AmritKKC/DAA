import time
import random
from matplotlib import pyplot as plt


# Function to perform counting sort.
def counting_sort(A, B, k):
    c = [0] * (k + 1)   # Array to store count of each word.
    for j in range(len(A)):
        c[A[j]] += 1    # Adding 1 at index value equal to number in array.
    for i in range(1, k + 1):
        c[i] += c[i - 1]    # Adding count array value with its previous index value. 
    for j in range(len(A) - 1, -1, -1):
        B[c[A[j]] - 1] = A[j]   # Putting values in output array B in sorted order.
        c[A[j]] = c[A[j]] - 1   
    return B


x = [] 
t = []
for loop in range(1, 11):
    size = loop * 20000     # Array size.
    A = [random.randint(100, 900) for i in range(size)]
    B = [0 for i in range(len(A))]
    k = max(A)  # Maximum element in array.
    x.append(size)
    print(f'\nGiven Array: {A}')
    start = time.time_ns()
    counting_sort(A, B, k)  # Calling counting sort function.
    t.append((time.time_ns() - start)/10**3)
    print(f'\nSorted Array: {B}')
# Plotting graph
plt.title("Time Complexity Graph\nCounting Sort V/s O(n)")
plt.xlabel('Input Length (N)')
plt.ylabel('Time (in nano seconds)')
plt.plot(x, x, label='O(n)')
plt.plot(x, t, label='Counting Sort')
plt.legend()
plt.show()
