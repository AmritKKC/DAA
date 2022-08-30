def find(g, node):
    if g[node] < 0:
        return node
    else:
        temp = find(g, g[node])
        g[node] = temp
        return temp


def union(g, a, b, d, ans):
    ta = a
    tb = b
    a = find(g,a)
    b = find(g,b)
    if a == b:
        pass
    else:
        ans.append([ta, tb, d])
        if g[a] < g[b]:
            g[a] = g[a] + g[b]
            g[b] = a
        else:
            g[b] = g[a] + g[b]
            g[a] = b


weight_data = [[1, 2, 28], [2, 3, 16], [2, 7, 14], [3, 4, 12], [1, 6, 10], [7, 5, 24], [6, 5, 25], [7, 4, 18], [5, 4, 22]]
n = len(weight_data)
weight_data = sorted(weight_data, key=lambda weight_data: weight_data[2])
ans = []
g = [-1] * (n+1)
for u, v, d in weight_data:
    union(g, u, v, d, ans)
ans = sorted(ans, key=lambda ans: ans[2])
print("Vertices", ": ", "Cost")
for item in ans:
    for i,j,k in [item]:
        print(i, " - ", j, " : ", k)
