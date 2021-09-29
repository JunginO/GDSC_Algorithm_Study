"""
알파벳 갯수 26개...
a=chr(97)
print(a)
반대는 ord('a')
"""
n=int(input())

count=0
for _ in range(n):
    b=True
    alpha=[0 for i in range(26)]
    word=list(input())
    for k in range(len(word)):
        for i in range(97,123):
            if (word[k]==chr(i)):
                if (alpha[i-97]==0):
                    alpha[i-97]=1
                elif(alpha[i-97]==1):
                    if(word[k-1]!=word[k]):
                        b=False
                        break
            else:
                pass
    if (b):
        count+=1
    word.clear()
    alpha.clear()
print(count)


    