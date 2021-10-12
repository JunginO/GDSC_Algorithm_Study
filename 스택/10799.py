n=list(input())
st=[]
ans=0
for i in range(len(n)):
    if n[i]=="(":
        st.append("(")
    else:
        if n[i-1]=="(":
            st.pop()
            ans+=len(st)
        else:
            st.pop()
            ans+=1
print(ans)