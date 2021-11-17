import sys
import heapq

n=int(input())
lft=[]
rgt=[]
for i in range(n):
    tmp=int(sys.stdin.readline())
    if len(lft)==len(rgt):
        heapq.heappush(lft,-tmp)
    else:
        heapq.heappush(rgt,tmp)
    if rgt and -lft[0]>rgt[0]:
        heapq.heappush(lft,-heapq.heappop(rgt))
        heapq.heappush(rgt,-heapq.heappop(lft))
    print(-lft[0])

#힙은 부모가 두 자식들보다 크지 않은 것을 보장하는 것이지,
# 자식들간의 대소는 보장하지 않습니다. 

