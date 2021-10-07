n=int(input())
lst=[]
for _ in range(n):
    tmp=list(map(int,input().split()))
    lst.append(tmp)
lst.sort(key=lambda x:(x[0],x[1]))
for x,y in lst:
    print(x,y) 