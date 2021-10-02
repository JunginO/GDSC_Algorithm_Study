   

def mergeSort(lst):
    if len(lst) <=1:
        return lst
    mid = len(lst)//2
    left=mergeSort(lst[:mid])
    right=mergeSort(lst[mid:])
    result=[]
    while len(left)>0 or len(right)>0:
        if len(left)>0 and len(right)>0:
            if left[0]<=right[0]:
                result.append(left[0])
                left=left[1:]
            else:
                result.append(right[0])
                right=right[1:]
        elif len(left)>0:
            result.append(left[0])
            left=left[1:]
        elif len(right)>0:
            result.append(right[0])
            right=right[1:]
    return result


n=int(input())
lst=[]
for _ in range(n):
    lst.append(int(input()))
lst=mergeSort(lst)

for i in lst:
    print(i)

    """
    시간초과로 실패,,,
    pypy3로 돌려도 실패,,,
    그냥 pypy로 sort돌려서 통과
    """