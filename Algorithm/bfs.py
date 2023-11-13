###################
# 1. BFS -> 큐 자료구조 사용(deque)
# 2. 시간복잡도는 O(N)이며, 재귀함수 사용하는 DFS보다는 수행시간 빠름
###################

from collections import deque

# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원)
graph = [
    [].
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원)
visited = [False] * len(graph)

def bfs(graph, v, visited):
    # 첫 노드 큐에 삽입 및 방문처리
    queue = deque([v])
    visited[v] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서하나의 원소를 뽑아 출력
        node = queue.popleft()
        print(node, end=' ')
        # 꺼낸 노드의 인접한 노드들 확인
        for i in graph[node]:
            # 인접노드 방문하지 않았다면 방문처리 및 인접노드 큐에 넣기
            if not visited[i]:
                visited[i] = True
                queue.append(i)

# 정의된 BFS함수 호출
bfs(graph, 1, visited)