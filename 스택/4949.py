import sys
while(True):
    n=list(sys.stdin.readline().rstrip())
    if (len(n)==1 and n[0]=='.'):#종료조건 확인해주기
        break
        
    st=[]
    ans=True
    for i in n:#문자열로 받아온 리스트 원소를 하나씩 검사
        if i=='('or i=='[':#'('이거나'['이면 스택에 넣는다
            st.append(i)
        elif i==')':#')'일경우
            if not st:#스택이 비어있는지 확인하고
                ans=False
                break
            if st.pop()!='(':#pop한 요소가 '('가 맞는지 확인
                ans=False
                break
        elif i==']':#']'일경우
            if not st:#스택이 비어있는지 확인하고
                ans=False
                break
            if st.pop()!='[':#pop한 요소가 '['가 맞는지 확인 
                ans=False
                break
    if st:#for문이 끝나고 스택이 비어있는지 확인
        ans=False
    if ans:#출력
        print("yes")
    else:
        print("no")

    