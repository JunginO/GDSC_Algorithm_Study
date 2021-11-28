import sys
sys.setrecursionlimit(5000000)
#ab=[[-1, -1], [-1, 0], [-1, 1], [0, -1],  [0, 1], [1, -1], [1, 0], [1, 1]]
def dfs(a,b):
    if 0<=a<h and 0<=b<w:
        if graph[a][b]==1:
            graph[a][b]=0
            dfs(a-1, b-1)
            dfs(a-1, b)
            dfs(a-1, b+1)
            dfs(a,b-1)
            dfs(a, b+1)
            dfs(a+1, b-1)
            dfs(a+1, b)
            dfs(a+1, b+1)
            return True
            """            
            for k in range(8):
                da=a+ab[k][0]
                db=b+ab[k][1]
                dfs(da,db)
                return True
                """
        return False
while(True):
    w,h=map(int,input().split())
    if(w==0 and h==0):
        break
    graph=[]
    cnt=0
    for _ in range(h):
        width=list(map(int,input().split()))
        graph.append(width)
    
    for i in range(h):
        for j in range(w):
            if dfs(i,j)==True:
                cnt+=1

    print(cnt)
