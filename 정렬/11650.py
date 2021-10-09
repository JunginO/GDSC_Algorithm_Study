import sys

n=int(sys.stdin.readline())
lst=[]
for _ in range(n):
    tmp=list(map(int,sys.stdin.readline().split()))
    lst.append(tmp)
lst.sort(key=lambda x:(x[0],x[1]))
for x,y in lst:
    print(x,y) 