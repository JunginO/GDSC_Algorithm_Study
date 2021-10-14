import sys
n=int(input())
lst=list(map(int,sys.stdin.readline().split()))
st=[]
ans=[0 for i in range(n)]

st.append([lst[0],0])
for i in range(1,n):   
    while st:
        if st[-1][0]>=lst[i]:
            ans[i]=st[-1][1]+1
            break
            
        else:
            st.pop()
    st.append([lst[i],i])

            
for i in ans:
    print(i,end=" ")