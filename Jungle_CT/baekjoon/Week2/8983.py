from sys import stdin
import bisect


def can_catch(animal_x, animal_y, gun_pos, L):
    """동물이 총으로 잡힐 수 있는지 확인"""
    return abs(animal_x - gun_pos) + animal_y <= L


N, M, L = map(int, stdin.readline().split())
gun = list(map(int, stdin.readline().split()))
gun.sort()

total = 0

for i in range(M):
    x, y = map(int, stdin.readline().split())
    
    # 이진 탐색으로 가장 가까운 총 찾기
    idx = bisect.bisect_left(gun, x)
    
    # 왼쪽과 오른쪽 총들을 확인
    candidates = []
    if idx > 0:
        candidates.append(gun[idx - 1])
    if idx < len(gun):
        candidates.append(gun[idx])
    
    # 후보 총들 중에서 잡을 수 있는 것이 있는지 확인
    for gun_pos in candidates:
        if can_catch(x, y, gun_pos, L):
            total += 1
            break

print(total)