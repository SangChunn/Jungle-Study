from sys import stdin

results = []  # 결과를 저장할 리스트

while True:
    line = stdin.readline().strip()
    if line == '0':  # 입력이 0이면 종료
        break
    
    arr = list(map(int, line.split()))
    n = arr[0]  
    heights = arr[1:]  
    results.append(heights)  # 결과를 리스트에 저장

# 모든 입력을 받은 후 한번에 출력
for result in results:
    print(result)