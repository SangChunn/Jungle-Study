N = int(input())
check_list = list(map(int, input().split())) 
M = int(input())
ans_list = list(map(int, input().split()))

check_list.sort()

def binary(target, data):
    start = 0
    data = check_list
    end = len(data) - 1

    while start <= end:
        mid = (start + end) // 2

        if data[mid] == target:
            return target
    
        elif data[mid] < target:
            start = mid +1
        else:
            end = mid - 1
    return 

for i in ans_list:
    if (binary(i, check_list)):
        print(1)
    else:
        print(0)