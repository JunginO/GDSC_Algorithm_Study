n=int(input())
def fivo(i):
    if i==0 or i==1:
        return i
    else:      
        return fivo(i-1)+fivo(i-2)
print(fivo(n))
