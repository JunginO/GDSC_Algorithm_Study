#첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 
# 간선의 개수 M(1 ≤ M ≤ 10,000), 
# 탐색을 시작할 정점의 번호 V가 주어진다.

n,m,v=map(int,input().split())
graph=[[0]*(n+1) for _ in range(n+1)]
visited=[False]*(n+1)

for _ in range(m):
    x,y=map(int,input().split())
    graph[x][y]=1
    graph[y][x]=1

def dfs(v):
    visited[v]=True #탐색시작한 정점 체크
    print(v,end=" ")
    for i in range(1,n+1):
        if not visited[i] and graph[v][i]==1:#방문한 정점이 아니고
            #지금 점이랑 연결되어있을경우
            dfs(i)

def bfs(v):
    visited[v]=True 
    queue=[v]#큐에다가 시작점 넣기
    while queue:
        v=queue.pop(0)#큐 첫번째 팝
        print(v,end=" ")
        for i in range(1,n+1):
            if not visited[i] and graph[v][i]==1:
                #방문한 정점이 아니고 그래프가 연결되어있으면
                #큐에 점 추가
                #방문했다고 추가,,,
                queue.append(i)
                visited[i]=True
        #n+1까지 다 돌고난다음 큐가 빌때까지,,,
dfs(v)
print()
visited=[False]*(n+1)
bfs(v)