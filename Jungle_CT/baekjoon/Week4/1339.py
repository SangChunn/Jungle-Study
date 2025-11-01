import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input())
words = [input().strip() for _ in range(N)]

first_pos = {}             # 가장 앞쪽 자리수 기록
count = defaultdict(int)   # 전체 등장 횟수

for w in words:
    length = len(w)
    for idx, ch in enumerate(w):
        count[ch] += 1
        # (길이 - idx) 값이 클수록 더 왼쪽(자리수가 큼)
        pos_val = length - idx
        if ch not in first_pos or pos_val > first_pos[ch]:
            first_pos[ch] = pos_val

# 각 알파벳을 정렬: 앞쪽 자리수 큰 순 -> 등장 횟수 큰 순
letters = sorted(first_pos.keys(),
                 key=lambda c: (first_pos[c], count[c]),
                 reverse=True)

# 9부터 내려가며 매핑
digit = 9
mapping = {}
for ch in letters:
    mapping[ch] = digit
    digit -= 1

# 단어들을 숫자로 변환 후 합산
ans = 0
for w in words:
    num = 0
    for ch in w:
        num = num * 10 + mapping[ch]
    ans += num

print(ans)