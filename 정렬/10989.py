"""
    입력을 받을 때에는 
    n = int(input()) 보다는
    from sys import stdin
    n = int(stdin.readline())
    가 훨신 빠르다고 한다

    빈 리스트에 append()로 추가하는것보다 초기화된 리스트에 인덱스를 이용하여 
    접근, 입력받는것이 낫다

    ->값을 입력받으면 메모리가 초과!!
    인덱스로 값을 표현하는 방법을 사용

    Pypy를 쓸 경우 print가 아니라 sys.stdout.write 쓰라고 함

"""
import sys
n=int(sys.stdin.readline())
lst=[0 for i in range(10001)]

for i in range(n):
    lst[int(sys.stdin.readline())]+=1

for i in range(10001):
    if lst[i]>0:
        for _ in range(lst[i]):
            print(i)