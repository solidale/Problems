adj = [
    [1, 2], 
    [0, 2, 3],
    [0, 1, 4],
    [1, 4],
    [2, 3]
]

def bfs(adj: list[list[int]], start: int):
    visited = [False] * len(adj)
    visited[start] = True
    queue = []

    queue.append(start)

    while len(queue) > 0:
        current_position = queue.pop(0)
        print(current_position)
        for neighbor in adj[current_position]:
            if visited[neighbor] == False:
                visited[neighbor] = True
                queue.append(neighbor)
            

bfs(adj, 0)