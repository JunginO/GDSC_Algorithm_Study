"""import sys
n=int(sys.stdin.readline())
def fiv(n):
        if n==1:
            global one_cnt
            one_cnt+=1
            return 1
        elif n==0:
            global zero_cnt
            zero_cnt+=1
            return 0
        else:
            return fiv(n-2)+fiv(n-1)
for _ in range(n):
    one_cnt=0
    zero_cnt=0
    i=int(sys.stdin.readline())
    fiv(i)
    print(zero_cnt,one_cnt)"""

t=int(input())#테스트케이스 갯수
zero=[1,0,1]
one=[0,1,1]

def fibo(num):
    length=len(zero)
    if num>=length:
        for i in range(length,num+1):
            zero.append(zero[i-1]+zero[i-2])
            one.append(one[i-1]+one[i-2])
    print(zero[num],one[num])


for i in range(t):

    n=int(input())
    fibo(n)