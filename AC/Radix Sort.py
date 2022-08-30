import time
import random
from matplotlib import pyplot as plt


# Function to perform counting sort.
def counting_sort(arr, exp):
    n = len(arr)
    c = [0] * 10    # Array to store count of each word.
    b = [0] * n     # Array to store output.
    for j in range(n):
        index = arr[j] // exp
        c[index % 10] += 1  # Taking modulus to get digit at preferred ones, tens, hundreds.. positions.
    for x in range(1, 10):
        c[x] += c[x-1]      # Adding count array value with its previous index value.
    for i in range(n-1, -1, -1):
        index = arr[i] // exp
        b[c[index % 10] - 1] = arr[i]   
        c[index % 10] -= 1
    for i in range(n):
        arr[i] = b[i]   # Putting values in array in sorted order according to digits of number.


def radix_sort(arr):
    m = max(arr)    # Maximum value in array.
    exp = 1     # Taking variable to help in passing the digit of numbers.
    while m / exp > 1:
        counting_sort(arr, exp)     # Calling counting sort function.
        exp *= 10   # Increasing value with multiple of 10.


x = []
t = []
for loop in range(1, 11):
    size = loop * 20000     # Array size.
    arr = [random.randint(1, 900) for i in range(size)]
    x.append(size)
    print(f'\nGiven Array: {arr}')
    start = time.time_ns()
    radix_sort(arr)     # Calling Radix Sort function.
    t.append((time.time_ns() - start)/10**3.6)
    print(f'\nSorted Array: {arr}')
# Graph Plot
plt.title("Time Complexity Graph\nRadix Sort V/s O(n)")
plt.xlabel('Input Length (N)')
plt.ylabel('Time (in nano seconds)')
plt.plot(x, x, label='O(n)')
plt.plot(x, t, label='Radix Sort')
plt.legend()
plt.show()
