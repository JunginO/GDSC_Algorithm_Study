from collections import deque
n=int(input())
lst=deque([i+1 for i in range(n)])
for _ in range(n):
    if len(lst)==1:
        break
    lst.popleft()
    lst.append(lst.popleft())
for i in lst:
    print(i)
