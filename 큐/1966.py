from collections import deque
testCaseNum=int(input())
for _ in range(testCaseNum):
    n,m=map(int,input().split())
    tmp=deque(list(map(int, input().split())))
    index=[0 for _ in range(n)]
    index[m]=1
    cnt=1
    while True:
        if tmp[0]==max(tmp):
            if index[0]==1:
                break
            else:
                index.pop(0)
                tmp.popleft()
                cnt+=1
        else:
            tmp.append(tmp.popleft())
            index.append(index.pop(0))
    print(cnt)