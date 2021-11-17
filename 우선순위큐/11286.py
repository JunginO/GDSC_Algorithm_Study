import sys
import heapq

n=int(sys.stdin.readline().rstrip())
heap=[]
for _ in range(n):
    tmp=int(sys.stdin.readline())
    if tmp==0:
        try:
            result=heapq.heappop(heap)
            print(result[1])
        except:
            print(0)

    else:
        heapq.heappush(heap, (abs(tmp),tmp))
