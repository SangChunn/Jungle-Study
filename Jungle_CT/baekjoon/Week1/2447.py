N = int(input())

def star(n):
    if n == 1:
        return ['*']
    else:
        cur = star(n//3)
        top_bottom = [x*3 for x in cur]
        middle = [x + ' ' *(n//3)+ x for x in cur]

        return top_bottom + middle + top_bottom



print('\n'.join(star(N)))
