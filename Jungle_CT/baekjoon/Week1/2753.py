date = int(input())

if (date % 4 == 0 and date % 100 != 0):
    print('1')
elif (date % 400 == 0):
    print('1')
else:
    print('0')
