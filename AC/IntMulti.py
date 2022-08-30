# Design and Analysis of Algorithm Assignment 2.
# Program to perform Integer Multiplication using Divide and Conquer.
# Plot the graph for running time taken by algorithm for different input sizes.
# Compare the curve with the curve of n^2 and n^1.6.

def multiply(x, y):
    x = str(x)
    y = str(y)
    l1 = len(x)  # Length of first user input.
    l2 = len(y)  # Length of second user input.
    # Making input length even if it is odd.
    if l1 == l2:
        if l1 != 1:
            if l1 % 2 != 0:
                x = '0' + x
                l1 = l1 + 1
    else:
        if l1 > l2:
            if l1 % 2 != 0:
                x = '0' + x
                l1 = l1 + 1
        elif l1 < l2:
            if l2 % 2 != 0:
                y = '0' + y
                l2 = l2 + 1
    n = max(l1, l2)
    # Making length of both inputs equal by adding 0 at start of input.
    if l1 < l2:
        x = '0' * (l2 - l1) + x
        l1 = l1 + (l2 - l1)
    elif l1 > l2:
        y = '0' * (l1 - l2) + y
        l2 = l2 + (l1 - l2)

    # Base Condition
    if n == 1:
        return int(x) * int(y)

    xL = x[:n // 2]  # Taking left part of first input.
    xR = x[n // 2:]  # Taking right part of first input.
    yL = y[:n // 2]  # Taking left part of second input.
    yR = y[n // 2:]  # Taking right part of second input.

    # Using recursion for multiplication.
    P1 = multiply(xL, yL)
    P2 = multiply(xR, yR)
    P3 = multiply(int(xL) + int(xR), int(yR) + int(yL))
    # return int(P1 * 2 ** n + (P3 - P1 - P2) * 2 ** (n / 2) + P2)  # Use this for binary input.
    return int(P1 * 10 ** n + (P3 - P1 - P2) * 10 ** (n / 2) + P2)  # Use this for integer input.


x = int(input("Enter first number: "))  # Taking first input from user.
y = int(input("Enter second number: "))  # Taking second input from user.
print("Output:", multiply(x, y))  # Calling multiply function.
