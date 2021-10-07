lst=[]
diff=0
for _ in range(9):
    lst.append(int(input()))

flag=False
    
diff=sum(lst)-100
for i in range(8):
    for j in range(i+1,9):
        if (lst[i]+lst[j])==diff:
            lst.remove(lst[j])
            lst.remove(lst[i])
            flag=True
            break
    if(flag):break
lst.sort()
for i in lst:
    print(i)
