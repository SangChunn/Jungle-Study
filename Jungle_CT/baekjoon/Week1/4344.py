N = int(input().strip())
case = [list(map(int,input().split())) for _ in range(N)]
for data in case:
    score = data[1:]
    people = data[0]
    avg = sum(score) / people
    up = sum(1 for s in score if s > avg)
    rate = up / people * 100
    print(f"{rate:.3f}%")

