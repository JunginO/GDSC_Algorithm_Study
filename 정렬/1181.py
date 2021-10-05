n=int(input())
lst=[]
for _ in range(n):
    lst.append(input())
lst=set(lst)
lst=list(lst)
lst.sort()
lst.sort(key=len)
for i in lst:
    print(i)