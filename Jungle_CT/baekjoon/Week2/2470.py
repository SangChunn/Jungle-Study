# 산성  양의 정수
# 알칼리성 음의 정수
from sys import stdin

def binary_search(arr, target, start, end):
    """target과 가장 가까운 값을 찾는 binary search"""
    left, right = start, end
    closest = arr[start]
    min_diff = abs(arr[start] - target)

    while left <= right:
        mid = (left + right) // 2
        current_diff = abs(arr[mid] - target)
        
        if current_diff < min_diff:
            min_diff = current_diff
            closest = arr[mid]
        
        if arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            return arr[mid]
    
    return closest

N = int(input())
num_list = list(map(int, stdin.readline().split()))

# 정렬 (binary search를 위해 필요)
num_list.sort()

min_diff = float('inf')
result = [0, 0]

# 각 원소에 대해 그 원소와 합이 0에 가장 가까운 다른 원소를 찾기
for i in range(N):
    current = num_list[i]
    # 현재 원소를 제외한 나머지 원소들에서 -current와 가장 가까운 값 찾기
    target = -current
    
    # 현재 원소를 제외한 배열에서 binary search
    if i == 0:
        closest = binary_search(num_list, target, 1, N-1)
    elif i == N-1:
        closest = binary_search(num_list, target, 0, N-2)
    else:
        # 현재 원소 앞쪽과 뒤쪽에서 각각 찾아서 더 가까운 것 선택
        left_closest = binary_search(num_list, target, 0, i-1)
        right_closest = binary_search(num_list, target, i+1, N-1)
        
        if abs(left_closest - target) < abs(right_closest - target):
            closest = left_closest
        else:
            closest = right_closest
    
    current_sum = current + closest
    current_diff = abs(current_sum)
    
    if current_diff < min_diff:
        min_diff = current_diff
        result = [current, closest]

# 결과 출력 (오름차순으로)
print(*sorted(result))
########################################################

from sys import stdin
from bisect import bisect_left

# 1. 입력 & 정렬
N = int(input().strip())
arr = list(map(int, stdin.readline().split()))
arr.sort()

# 2. 결과 변수
best_sum = float('inf')
ans = (0, 0)

# 3. 이진탐색으로 가장 가까운 값 찾기
def binary_search_closest(array, target):
    """정렬된 array에서 target과 가장 가까운 값을 반환"""
    idx = bisect_left(array, target)  # target 삽입 위치
    candidates = []
    if idx < len(array):
        candidates.append(array[idx])
    if idx > 0:
        candidates.append(array[idx-1])
    # candidates 중 target과 차이가 가장 작은 값 리턴
    return min(candidates, key=lambda x: abs(x - target))

# 4. 모든 원소에 대해 -a와 가까운 값 찾기
for i, a in enumerate(arr):
    target = -a
    # 자기 자신을 제외하기 위해 후보를 직접 확인
    # j-1, j, j+1 대신 함수 재사용 + 인덱스 체크
    idx = bisect_left(arr, target)

    # idx 주변 원소를 살피면서 자기 자신 제외
    for k in (idx-1, idx):
        if 0 <= k < N and k != i:
            s = a + arr[k]
            if abs(s) < abs(best_sum):
                best_sum = s
                ans = (a, arr[k])
                if best_sum == 0:   # 0이면 최적이므로 바로 종료 가능
                    break

print(*sorted(ans))