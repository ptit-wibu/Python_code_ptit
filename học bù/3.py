from collections import deque
import sys
input = sys.stdin.readline

def bfs(graph, start, target, banned):
    visited = [False] * len(graph)
    queue = deque([start])
    visited[start] = True

    while queue:
        node = queue.popleft()
        if node == target:
            return True
        for i in graph[node]:
            if not visited[i] and i != banned:
                visited[i] = True
                queue.append(i)
    return False

def solve(N,M,u,v,edges):
    graph = [[] for _ in range(N+1)]
    for a, b in edges:
        graph[a].append(b)

    cnt= 0
    for x in range(1, N+1):
        if x == u or x == v:
            continue
        if not bfs(graph, u, v, x):
            cnt += 1
    return cnt

test = int(input())
for _ in range (test):
    N, M, u, v = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range (M)]
    print(solve(N,M,u,v,edges))