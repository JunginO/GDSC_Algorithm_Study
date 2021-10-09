n=int(input())
st=[]
for _ in range(n):
	tmp=int(input())
	if tmp!=0:
		st.append(tmp)
	else:
		st.pop()
print(sum(st))