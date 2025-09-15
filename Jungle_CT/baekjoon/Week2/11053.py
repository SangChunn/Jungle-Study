A = int(input())
B = list(map(int, input().split())) 

dp = [0] * A  # dp[i]: i번째 원소로 끝나는 가장 긴 증가하는 부분 수열의 길이

for i in range(A):
    for j in range(i):
        if B[i] > B[j]:  # B[i]가 B[j]보다 클 때만 증가하는 부분 수열 가능
            # dp[i]와 dp[j] + 1 중 더 큰 값을 선택
            # dp[i]: 현재까지의 최대 길이
            # dp[j] + 1: j번째 원소 뒤에 i번째 원소를 붙인 길이
            dp[i] = max(dp[i], dp[j] + 1)

# dp 배열의 최댓값 + 1 (자기 자신도 포함해야 하므로)
print(max(dp)+1)
