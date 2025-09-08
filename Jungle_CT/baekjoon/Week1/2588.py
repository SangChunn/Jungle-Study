a = int(input().strip())
b = int(input().strip())

ones = b % 10
tens = (b // 10) % 10
hundreds = b // 100

print(a * ones)      # 1의 자리
print(a * tens)      # 10의 자리
print(a * hundreds)  # 100의 자리
print(a * b)         # 전체 곱
