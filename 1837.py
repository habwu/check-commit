from collections import deque, defaultdict
def bfs(graph, start):
    distances = {}
    distances[start] = 0
    queue = deque([start])
    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if neighbor not in distances:
                distances[neighbor] = distances[current] + 1
                queue.append(neighbor)
    return distances

n = int(input().strip())
graph = defaultdict(set)
all_people = set()
for _ in range(n):
    team = input().strip().split()
    all_people.update(team)

    for i in range(3):
        for j in range(i + 1, 3):
            graph[team[i]].add(team[j])
            graph[team[j]].add(team[i])
if "Isenbaev" in graph:
    distances = bfs(graph, "Isenbaev")
else:
    distances = {}
sorted_people = sorted(all_people)
for person in sorted_people:
    if person in distances:
        print(f"{person} {distances[person]}")
    else:
        print(f"{person} undefined")
