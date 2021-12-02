t=int(input())
def dp(i):
    if i==1:
        return 1
    elif i==2:
        return 2
    elif i==3:
        return 4
    else:
        return dp(i-1)+dp(i-2)+dp(i-3)
for _ in range(t):
    n=int(input())
    print(dp(n))
