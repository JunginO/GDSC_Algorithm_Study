n=int(input())
cnt=0
flag=True
while(True):
    if (n%5==0):
        break
    elif (n<0):
        flag=False
        break
    n-=3
    cnt+=1
if(flag):
    cnt+=(n/5)
    print(int(cnt))
else:
    print(-1)