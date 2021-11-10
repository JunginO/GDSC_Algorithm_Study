"""n,k=map(int,input().split())
lst=[i+1 for i in range(n)]
ans=[]
cnt=k-1
while(lst):
    if cnt>=len(lst):
        cnt=cnt%len(lst)
    if len(lst)==1:
        ans.append(lst.pop())
    else:        
        ans.append(lst[cnt])
        del lst[cnt]
        cnt+=k-1
print("<"+', '.join(map(str,ans))+">")"""
from collections import deque
n,k=map(int,input().split())
lst=deque([i+1 for i in range(n)])
ans=[]
cnt=1
while(lst):
    if cnt!=k:
        lst.append(lst.popleft())
        cnt+=1
    else:
        ans.append(lst.popleft())
        cnt=1

print("<"+', '.join(map(str,ans))+">")