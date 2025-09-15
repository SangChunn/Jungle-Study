from sys import stdin
A, B, C = map(int, stdin.readline().split())

def DaC(A, B, C):  # 분할정복을 이용한 빠른 거듭제곱
    if B == 1:
        return A % C
    
    # B//2를 한 번만 계산
    half = DaC(A, B // 2, C)
    
    if B % 2 == 0:  # B가 짝수
        return (half * half) % C
    else:  # B가 홀수
        return (half * half * A) % C

print(DaC(A, B, C))