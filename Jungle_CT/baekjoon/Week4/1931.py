#N개의 회의, 각 회의 I에 대해 시작시간과 끝나는 시간 -> 회의가 겹치지 않게 하는 최대 개수
# start 오름차순 정렬 후 end 값이 작은걸 뽑으면서 그걸 다시 업데이트해주고 그 엔드 값보다 큰 스타트 값에서 제일 작은 엔드값 선택
# 그리고 스타트 값이 제일 크거나 엔드값이 다른 스타트 값보다 크면 break
import sys
input = sys.stdin.readline
N = int(input())
time = []
for i in range(N):
    s, e = map(int, input().split())
    time.append((s,e))
time_table = sorted(time, key=lambda x : (x[1], x[0]))   # 왜 x[0] 을 더 써야되는지 모르겠어요
count = 0
end_time = 0

for s, e in time_table:
    if s >= end_time:
        count += 1
        end_time = e

print(count)