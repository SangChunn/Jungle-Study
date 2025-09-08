N = int(input())
total = 0
for i in range(1, N+1):
    num_list = list(map(int, str(i)))
    if (i < 100):
        total += 1
    elif(num_list[1]-num_list[0] == num_list[2]-num_list[1]):
        total += 1
print(total)