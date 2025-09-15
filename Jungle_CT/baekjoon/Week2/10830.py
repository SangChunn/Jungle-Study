# 1초 1억개 log n 가능
# N * N , B만큼 제곱
from sys import stdin

N, B = map(int, stdin.readline().split())
A = [list(map(int, stdin.readline().split())) for _ in range(N)]

def matrix_multiply(A, B):
    """행렬 곱셈 함수"""
    n = len(A)
    result = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += A[i][k] * B[k][j]
            result[i][j] %= 1000
    return result

def matrix_power(A, B):
    """분할정복을 이용한 행렬의 B제곱 - O(log B)"""
    n = len(A)
    
    # B가 1이면 원본 행렬 반환 (각 원소를 1000으로 나눈 나머지)
    if B == 1:
        result = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                result[i][j] = A[i][j] % 1000
        return result
    
    # B가 짝수면: A^B = (A^(B/2))^2
    if B % 2 == 0:
        half = matrix_power(A, B // 2)
        return matrix_multiply(half, half)
    
    # B가 홀수면: A^B = A * A^(B-1)
    else:
        return matrix_multiply(A, matrix_power(A, B - 1))

# 결과 계산 및 출력
result = matrix_power(A, B)
for row in result:
    print(' '.join(map(str, row)))