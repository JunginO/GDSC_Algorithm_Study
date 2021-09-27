n=int(input())
ans=[]
for _ in range(n):
    lst=list(input())
    r,l=0,0
    for i in range(len(lst)):
        if lst[i]=="(":
            l+=1
        elif lst[i]==")":
            r+=1
        
        if r>l:
            r+=1
    if r==l:
        ans.append('YES')
    else:
        ans.append('NO')
    lst.clear()
for i in ans:
    print(i)
    