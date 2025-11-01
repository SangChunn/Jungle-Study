# + -> 최대 최대 -> 최대 , 최소 최소 -> 최소
# - -> 최대 최소 -> 최대 , 최소 최대 -> 최소
# X -> 최대 최대 or 최소 최소 -> 최대
#   -> 최대 최소 , 최소 최대 , 최소 최소 -> 최소
# i j k l 구간 나누기 요게 중요할듯
import sys
input = sys.stdin.readline

total_list = input().strip()
num_list = []
ops = []
mn_list = []
mx_list = []
num = ""
for i in total_list:
    if i.isdigit():
        num += i
    else:
        num_list.append(int(num))
        ops.append(i)
        num = ""
num_list.append(int(num))

def calc(a, op, b):
    if op == '+': return a + b
    if op == '-': return a - b
    if op == '*': return a * b

n = len(num_list)
min_list = [[0] * n for _ in range(n)]
max_list = [[0] * n for _ in range(n)]

for i in range(n):
    min_list[i][i] = max_list[i][i] = num_list[i]

for i in range(2, n+1):
    for j in range(n-i+1):
        k = i + j -1
        min_list[j][k] = float("inf")
        max_list[j][k] = float("-inf")
        for l in range(j, k):
            op = ops[l]
            result = {
                calc(max_list[j][l], op, max_list[l+1][k]),
                calc(max_list[j][l], op ,min_list[l+1][k]),
                calc(min_list[j][l], op, max_list[l+1][k]),
                calc(min_list[j][l], op, min_list[l+1][k])
            }
            min_list[j][k] = min(min_list[j][k], *result)
            max_list[j][k] = max(max_list[j][k], *result)
        mn_list.append(min_list[j][k])
        mx_list.append(max_list[j][k])
print(mx_list)
print(mn_list)
print(max_list[0][n-1])
