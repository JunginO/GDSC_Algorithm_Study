n=int(input())
add,sum=0,0

lst=list(map(int,input().split()))

lst.sort()
for i in lst:
    add+=i
    sum+=add
print(sum)
