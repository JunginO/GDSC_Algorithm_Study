import sys
n=int(input())
st=[]
for _ in range(n):
    t=sys.stdin.readline().rstrip()
 
    if 'push' in t:
        a,b=t.split()   
        st.append(b)
    elif 'top' in t:
        if len(st)==0:
            print('-1')
        else:
            print(st[-1])
    elif 'size' in t:
        print(len(st))
    elif 'empty' in t:
        if (len(st))==0:
            print('1')
        else:
            print(0)
    elif 'pop' in t:
        if len(st)==0:
            print('-1')
        else:
            print(st.pop())
