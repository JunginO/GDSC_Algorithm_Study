while True:
    try:
        n=input()
        print(n)
    except EOFError:#에러 예외처리
        break