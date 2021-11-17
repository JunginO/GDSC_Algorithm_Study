import sys
import heapq
import math

n=int(input())
heap=[]
ans=[]
for i in range(n):
    tmp=int(input())
    heapq.heappush(heap,tmp)
    idx=i/2
    print(heap)
    ans.append(heap[math.floor(idx)])

print(ans)
#힙은 부모가 두 자식들보다 크지 않은 것을 보장하는 것이지,
# 자식들간의 대소는 보장하지 않습니다. 