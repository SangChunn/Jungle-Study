N = int(input().strip())
test = [input().strip() for _ in range(N)] 

for OX in test:
    score = 0
    sum_score = 0
    for ox in OX:
        if ox == 'O':
            score += 1
            sum_score += score
        else:
            score = 0
    print(sum_score)
