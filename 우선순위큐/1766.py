"""위상정렬
1. 진입 차수가 0인 정점을 큐에 삽입한다
2. 큐에서 원소를 꺼내 해당 원소와 간선을 제거한다
3. 제거 이후에 진입 차수가 0이 된 정점을 큐에 삽입한다
4. 큐가 빌 때까지 2~3을 반복
"""
import heapq
heap=[]
ans=[]
n,m=map(int,input().split())
lst=[[] for i in range(n+1)]
indegree=[0 for i in range(n+1)]

for _ in range(m):
    x,y = map(int,input().split())
    lst[x].append(y)
    indegree[y]+=1
    
for i in range(1, n+1):
    if indegree[i]==0:
        heapq.heappush(heap,i)#진입 차수가 0인 정점먼저 큐에 삽입
while heap:#빌 때까지
    data = heapq.heappop(heap)#큐에서 원소를 꺼내 해당 원소와 간선을 제거
    ans.append(data)
    for  y in lst[data]:
        indegree[y]-=1
        if indegree[y]==0:
            heapq.heappush(heap,y)#진입 차수가 0이 된 정점을 큐에 삽입
for i in ans:
	print(i, end = ' ')
