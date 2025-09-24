import sys
from collections import deque
input = sys.stdin.readline
M, N, H = map(int, input().split())
graph = [[[]*M]*N for _ in range(H+1)]