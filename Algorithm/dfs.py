#######################
# 1. dfs -> 스택과 재귀함수 사용
# 2. 시간복잡도는 O(N)
#######################

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
visited = [False] * len(graph)

def dfs(graph, v, visited):
    # 시작노드 방문처리
    visited[v] = True
    print(v, end=' ')
    # 해당노드의 인접노드(들) 처리
    for i in graph[v]:
        if not visited[i]:
            visited[i] = True
            dfs(graph, i, visited)

    dfs(graph, 1, visited)