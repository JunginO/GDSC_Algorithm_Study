import sys
n=int(sys.stdin.readline())
q=[]
for _ in range(n):
    tmp=sys.stdin.readline()
    if " " in tmp:
        a,b=tmp.split()
        b=int(b)
        q.append(b)
    elif "front" in tmp:
        if not q:
            print(-1)
        else:
            print(q[0])
    elif "back" in tmp:
        if not q:
            print(-1)
        else:
            print(q[-1])
    elif "size" in tmp:
        print(len(q))
    elif "pop" in tmp:
        if not q:
            print(-1)
        else:
            print(q.pop(0))
    elif "empty" in tmp:
        if not q:
            print(1)
        else:
            print(0)
