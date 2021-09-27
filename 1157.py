"""알파벳 소문자 a=97
알파벳 대문자 26개 소문자26
A=65...65~90/97~122"""

lst=list(input())
tmplist=[]
cnt,ans=0,0
ss=0
for i in lst:
    tmp=ord(i)
    if tmp<91:
        tmp+=32
    tmplist.append(tmp)

for i in range(97,123):#a부터 z까지
    if (tmplist.count(i))>cnt:#현재 cnt보다 해당 알파벳값이 크면
        ans=i
        cnt=tmplist.count(i)
        ss=0#쌤쌤도 초기화
    elif ((tmplist.count(i))==cnt):#현재최고갯수랑 같은게나오면
        ss+=1#쌤쌤하나추가

if (ss>0):
    print('?')
else:
    ans-=32
    print(chr(ans))
