#######################
# 1. dfs -> 스택과 재귀함수 사용
# 2. 시간복잡도는 O(N)
#######################

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

# DFS 메서드 정의
def dfs(graph, v, visited):
    # 시작노드 방문처리
    visited[v] = True
    print(v, end=' ')
    # 해당노드의 인접노드(들) 처리
    for i in graph[v]:
        if not visited[i]:
            visited[i] = True
            dfs(graph, i, visited)
            
# 정의된 DFS 함수 호출
dfs(graph, 1, visited)