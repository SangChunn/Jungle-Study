a = int(input('정수 a: '))
b = int(input('정수 b: '))
c = int(input('정수 c: '))

max = a
if b > max : 
    max = b
if c > max:
    max = c

print(f'max: {max}')