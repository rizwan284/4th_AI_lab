from collections import deque

def bfs(capacity, start, goal):
    visited = set()
    queue = deque([(start[0], start[1], [])])

    while queue:
        x, y, path = queue.popleft()

        if (x, y) == goal:
            return path + [(x, y)]

        if (x, y) in visited:
            continue
        visited.add((x, y))

        moves = [
            (capacity[0], y), 
            (x, capacity[1]), 
            (0, y), 
            (x, 0),
            (x - min(x, capacity[1] - y), y + min(x, capacity[1] - y)), 
            (x + min(y, capacity[0] - x), y - min(y, capacity[0] - x))
        ]

        for move in moves:
            queue.append((move[0], move[1], path + [(x, y)]))

    return []

def water_jug(capacity, goal):
    start = (0, 0)
    return bfs(capacity, start, goal)

capacity = (4, 3)
goal = (2, 0)
result = water_jug(capacity, goal)
print(result)
