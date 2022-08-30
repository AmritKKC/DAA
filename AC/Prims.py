INF = 9999999
G = [[0, 5, 9, 7, 0],
     [5, 0, 10, 0, 8],
     [9, 10, 0, 20, 25],
     [7, 0, 20, 0, 11],
     [0, 8, 25, 11, 0]]
N = len(G)
selected_node = [0, 0, 0, 0, 0]
no_edge = 0
selected_node[0] = True
print("Edge : Weight")
while no_edge < N - 1:
    minimum = INF
    a = 0
    b = 0
    for m in range(N):
        if selected_node[m] == True:
            for n in range(N):
                if (not selected_node[n]) and G[m][n]:
                    # not in selected and there is an edge
                    if minimum > G[m][n]:
                        minimum = G[m][n]
                        a = m
                        b = n
    print(str(a) + " - " + str(b) + " : " + str(G[a][b]))
    selected_node[b] = True
    no_edge += 1
