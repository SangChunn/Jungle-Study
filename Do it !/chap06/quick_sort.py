def quick_sort(arr):
    # 원소가 1개 이하일 경우 그대로 반환
    if len(arr) <= 1:
        return arr
    
    # 피벗: 리스트의 첫 번째 원소
    pivot = arr[len(arr)//2]

    # 피벗 기준으로 작은 값과 큰 값 나누기
    left = [x for x in arr if x < pivot]
    mid   = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    # 재귀적으로 정렬 후 합치기
    return quick_sort(left) + mid + quick_sort(right)


# 예시 실행
nums = [3, 6, 8, 10, 1, 2, 1]
print(quick_sort(nums))




