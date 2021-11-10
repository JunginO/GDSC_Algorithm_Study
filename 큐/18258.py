from collections import deque
import sys
n=int(sys.stdin.readline().strip())
queue=deque()
for _ in range(n):
    tmp=sys.stdin.readline().strip()
    if 'push' in tmp:
        a,b=tmp.split()
        b=int(b)
        queue.append(b)
    elif 'pop' in tmp:
        if not queue:
            print(-1)
        else:
            print(queue.popleft())    
    elif 'size' in tmp:
        print(len(queue))
    elif 'empty' in tmp:
        if not queue:
            print(1)
        else:
            print(0)
    elif 'front' in tmp:
        if not queue:
            print(-1)
        else:
            print(queue[0])
    elif 'back' in tmp:
        if not queue:
            print(-1)
        else:
            print(queue[len(queue)-1])
    