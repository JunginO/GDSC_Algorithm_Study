import sys
import heapq

n=int(sys.stdin.readline())
heap=[]
for _ in range(n):
    tmp=int(sys.stdin.readline())
    if tmp==0:
        try:
            print(-1*heapq.heappop(heap))
        except:
            print(0)
            
    else:
        heapq.heappush(heap, (-tmp))
        