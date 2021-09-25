s=list(input())
ans=[]

for i in range(97,123):
    if chr(i) in s:
        for j in range(len(s)):
            if chr(i)==str(s[j]):
                ans.append(j)
                break
    else:
        ans.append(-1)

for i in ans:
    print(i,end=" ")

"""
알파벳 갯수 26개...
a=chr(97)
print(a)
반대는 ord('a')
"""