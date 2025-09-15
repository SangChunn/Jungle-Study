n = int(input())

def fibo(N):
    if N == 0:
        return 0
    if N == 1:
        return 1
    else:
        ans = fibo(N-1) + fibo(N-2) 
        return ans
print(fibo(n))