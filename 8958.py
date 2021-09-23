n=int(input())

for _ in range(n):
    score,total=0,0
    lst=list(input())
    for i in range(len(lst)):
        if lst[i]=='O':
            score+=1
            total+=score
        elif lst[i]=='X':
            score=0
    print(total)
    lst.clear()

