n=int(input())
graph=[]

for _ in range(n):
    graph.append(list(map(int,input().strip())))

ans=[]
dx=[0,0,1,-1]
dy=[1,-1,0,0]
cnt=0

def dfs(x,y):
    global cnt
    if x<=-1 or x>=n or y<=-1 or y>=n:
        return False
    if graph[x][y]==1:
        cnt+=1
        graph[x][y]=0
        for i in range(4):
            dfs(x+dx[i],y+dy[i])
        return True
    return False
        

for i in range(n):
    for j in range(n):
        if dfs(i,j):
            ans.append(cnt)
            cnt=0
print(len(ans))
ans.sort()
for i in ans:
    print(i)