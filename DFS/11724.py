import sys
sys.setrecursionlimit(10000)
n,m=map(int,sys.stdin.readline().split())
graph=[[0]*(n+1) for _ in range(n+1)]
visited=[False for _ in range(n+1)]
for _ in range(m): 
    u,v=map(int,sys.stdin.readline().split())
    graph[u][v]=1
    graph[v][u]=1
cnt=0
def dfs(v):
    visited[v]=True #탐색시작한 정점 체크
    for i in range(1,n+1):
        if not visited[i] and graph[v][i]==1:#방문한 정점이 아니고
            #지금 점이랑 연결되어있을경우
            dfs(i)
"""
visited[0]=True
while(not all(visited)):#all - 모든요소가 참 일 때까지,
    v=visited.index(False)#아직도 false인 첫번째요소
    dfs(v)
    cnt+=1
print(cnt) 굳이...
"""
for i in range(1,len(visited)):
    if visited[i]==False:
        dfs(i)
        cnt+=1
print(cnt)