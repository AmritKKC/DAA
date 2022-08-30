def _0_1_knapsack(values, weights, capacity):
    number_of_items = len(values)
    table = []
    for i in range(number_of_items):
        table.append([None] * capacity)
    for j in range(capacity):
        table[0][j] = 0
    for i in range(1, number_of_items):
        for j in range(capacity):
            if weights[i-1] > j:
                table[i][j] = table[i-1][j]
            else:
                table[i][j] = max(table[i-1][j], table[i-1][j-weights[i-1]] + values[i-1])
    return table[-1][-1]


values = [100, 60, 120]
weights = [20, 10, 30]
capacity = 50
print("Values: ", values)
print("Weights: ", weights)
print("Knapsack maximum capacity: ", capacity)
print("\nMaximum value taken: ", _0_1_knapsack(values, weights, capacity))
