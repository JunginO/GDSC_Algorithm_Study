import sys
left=list(sys.stdin.readline().rstrip())
num=int(input())

right=[]
for _ in range(num):
    i=list(sys.stdin.readline().split())

    if i[0]=='L':
        if left:
           right.append(left.pop())
    elif i[0]=="B":
        if left:
            left.pop()

    elif i[0]=="P":
        left.append(i[1])
    elif i[0]=="D":
        if right:
            left.append(right.pop())

print(''.join(left + list(reversed(right))))
