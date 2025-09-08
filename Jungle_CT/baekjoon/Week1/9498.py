score = int(input().strip())

if (90 <= score <= 100):
    print('A')
elif (89 >= score and score >= 80):
    print('B')
elif (79 >= score and score >= 70):
    print('C')
elif (69 >= score and score >= 60):
    print('D')
else:
    print('F')