def fractional_knapsack(value, weight, capacity):
    # index = [0, 1, 2, ..., n - 1] for n items
    index = list(range(len(value)))
    # Calculating ratios of values to weight.
    ratio = [v / w for v, w in zip(value, weight)]
    # Sorting index according to value-to-weight ratio in decreasing order
    index.sort(key=lambda i: ratio[i], reverse=True)
    max_v = 0   # Variable to store maximum value that can be taken
    item_fraction = [0] * len(value)    # Variable to store fractions of items that should be taken.
    for i in index:    # Using loop to check conditions for selecting items.
        if weight[i] <= capacity:
            item_fraction[i] = 1
            max_v += value[i]
            capacity -= weight[i]
        else:
            item_fraction[i] = capacity / weight[i]
            max_v += value[i] * capacity / weight[i]
            break

    return max_v, item_fraction


# Driver code.
n = int(input('Enter number of items: '))
value = input('Enter the values of items in order: ').split()
value = [int(v) for v in value]
weight = input('Enter the weights of items in order: ').split()
weight = [int(w) for w in weight]
capacity = int(input('Enter Knapsack Maximum Weight: '))
# Calling fractional knapsack function.
max_v, item_fraction = fractional_knapsack(value, weight, capacity)
print('Maximum value that can be taken:', max_v)    # Print max value that can be taken.
print('Fraction in which the items should be taken:', item_fraction)    # Print fractions of items selected.
