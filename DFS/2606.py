n=int(input())
graph=[[0]*(n+1) for _ in range(n+1)]
visited=[0 for _ in range(n+1)]
k=int(input())
for _ in range(k):
    i,j=map(int,input().split())
    graph[i][j]=1
    graph[j][i]=1

def dfs(c):
    visited[c]=1 
    for i in range(1,n+1):
        if visited[i]==0 and graph[c][i]==1:#방문한 정점이 아니고
            #지금 점이랑 연결되어있을경우
            dfs(i)
dfs(1)
print(visited.count(1)-1)