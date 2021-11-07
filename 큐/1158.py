n,k=map(int,input().split())
q=[ i for i in range(1,n+1)]
ans=[]
start=0
while q:
    start+=k-1
    if start>=len(q):
        start=start%len(q)
    ans.append(q.pop(start))
    
print("<"+', '.join(map(str,ans))+">")