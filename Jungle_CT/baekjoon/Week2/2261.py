from sys import stdin
import math

n = int(stdin.readline())
points = [list(map(int, stdin.readline().split())) for _ in range(n)]

def distance(p1, p2):
    """두 점 사이의 거리 계산"""
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2

def closest_pair_recursive(points):
    """분할정복으로 가장 가까운 두 점 찾기 - 모든 경우 분할정복"""
    n = len(points)
    
    # 기저 조건들
    if n <= 1:
        return float('inf')
    elif n == 2:
        return distance(points[0], points[1])
    
    # n >= 3인 경우도 분할정복으로 처리
    if n == 3:
        # 3개 점을 1개 + 2개로 분할
        left_min = closest_pair_recursive(points[:1])  # 1개 → 무한대
        right_min = closest_pair_recursive(points[1:])  # 2개 → 직접 계산
        cross_min = min(distance(points[0], points[1]),
                       distance(points[0], points[2]),
                       distance(points[1], points[2]))
        return min(left_min, right_min, cross_min)
    
    # x좌표로 정렬
    points.sort()
    
    # 중간점으로 분할
    mid = n // 2
    left_points = points[:mid]
    right_points = points[mid:]
    
    # 왼쪽과 오른쪽에서 각각 최단거리 구하기
    left_min = closest_pair_recursive(left_points)
    right_min = closest_pair_recursive(right_points)
    
    # 더 작은 거리
    min_dist = min(left_min, right_min)
    
    # 중간선 근처의 점들 확인
    mid_x = points[mid][0]
    candidates = []
    
    for point in points:
        if (point[0] - mid_x)**2 < min_dist:
            candidates.append(point)
    
    # y좌표로 정렬
    candidates.sort(key=lambda x: x[1])
    
    # 후보들 중에서 최단거리 확인
    for i in range(len(candidates)):
        for j in range(i+1, len(candidates)):
            # y좌표 차이가 min_dist보다 크면 더 이상 확인할 필요 없음
            if (candidates[j][1] - candidates[i][1])**2 >= min_dist:
                break
            dist = distance(candidates[i], candidates[j])
            min_dist = min(min_dist, dist)
    
    return min_dist

# 결과 출력
result = closest_pair_recursive(points)
print(result)