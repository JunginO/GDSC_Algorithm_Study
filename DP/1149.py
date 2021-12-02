n=int(input())
lst=[]
"""current=[0 for _ in range(n)]
def color(i,current,lst):
    for k in range(3):
        if lst[i][k]==min(lst[i][0],lst[i][1],lst[i][2]):
            if i!=0 and current[i-1]==k:

                lst[i][k]=1001
                return color(i,current,lst)                
            else:
                return k"""

for _ in range(n):
    r,g,b=map(int,input().split())
    lst.append([r,g,b])
for i in range(1, len(lst)):
    lst[i][0] = min(lst[i - 1][1], lst[i - 1][2]) + lst[i][0]
    lst[i][1] = min(lst[i - 1][0], lst[i - 1][2]) + lst[i][1]
    lst[i][2] = min(lst[i - 1][0], lst[i - 1][1]) + lst[i][2]
print(min(lst[n - 1][0], lst[n - 1][1], lst[n - 1][2]))