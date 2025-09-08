#########
def primenum(n):
    prime = [True] * (n + 1)
    prime[0] = prime[1] = False

    for i in range(2, int(n**0.5) + 1):
        if prime[i]:
            for j in range(i * i, n + 1, i):
                prime[j] = False
    return prime
###
def goldBach(n, prime):
    for a in range(n//2, 1, -1):
        b = n - a
        if prime[a] and prime[b]:
            return a, b

T = int(input().strip())
#일단 반으로 나누고 하나는 -1 하나는 +1 하면서 소수인지 확인하면 되지 않을까? 동시에 만족을 해야되는거지 
case =[int(input().strip()) for _ in range(T)]
prime = primenum(max(case))
for n in case:
    a, b = goldBach(n, prime)
    print(a, b)