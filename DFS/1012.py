import sys
sys.setrecursionlimit(10**9)
t=int(input())
xy=[[0,1],[0,-1],[-1,0],[1,0]]
def dfs(x,y):#그냥 x y로 하지말자,,,앞으론,,,
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False
    if graph[x][y]==1:
        graph[x][y]=0
        for i in range(4):
            dx=x+xy[i][0]
            dy=y+xy[i][1]
            dfs(dx,dy)
        return True
    return False

for _ in range(t):
    m,n,k=map(int,input().split())
    graph=[[0]*(m) for _ in range(n)]
    cnt=0
    for _ in range(k):
        x,y=map(int,input().split())
        graph[y][x]=1#수학에서 쓰는 (x,y)와 다르게 python 이차원 리스트에 접근 할 때에는 [y][x]순서

    for y in range(n):
        for x in range(m):
            if dfs(y,x):
                cnt+=1
    print(cnt)

    
