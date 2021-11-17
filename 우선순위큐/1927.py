import sys
import heapq

n=int(sys.stdin.readline())
heap=[]
for _ in range(n):
    tmp=int(sys.stdin.readline())
    if tmp==0:
        if len(heap)==0:
            print(0)
        else:
            result=heapq.heappop(heap)
            print(result)
    else:
        heapq.heappush(heap, tmp)
        