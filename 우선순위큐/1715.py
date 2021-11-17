import sys
import heapq
heap=[]
ans=0
n=int(input())
for _ in range(n):
    heapq.heappush(heap,int(input()))
while len(heap)>1:
    tmp1=heapq.heappop(heap)
    tmp2=heapq.heappop(heap)
    ans+=(tmp1+tmp2)
    heapq.heappush(heap,tmp1+tmp2)
print(ans)