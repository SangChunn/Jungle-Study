import re
expr = input().strip()
tokens = re.split(r'([+-])', expr)
tokens = ' '.join(tokens).split()

i = 0
result = 0
sign = +1

while i < len(tokens):
    if tokens[i] in '+-':
        i += 1
        continue

    num = int(tokens[i])
    if i > 0 and tokens[i-1] == '-':
        temp = num
        j = i + 1
        while j + 1 < len(tokens) and tokens[j] == '+':
            temp += int(tokens[j + 1])
            j += 2
        result -= temp
        i = j + 1  
    else:
        result += num
        i += 1

print(result)