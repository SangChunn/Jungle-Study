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
