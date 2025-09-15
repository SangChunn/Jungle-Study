from sys import stdin

 

# ('-')


# 27 -> 9 9 9
# 9 -> 3 3 3
# 81 -> 27 27 27
# 3**(N-1)+ 3**(N-1)

def cut_line(a, n):
    if n == 0:
        return ('-')
    else:
        for i in range(a +n//3, a + n//3*2):
            line[i] = ' '
        cut_line(a, n//3)
        cut_line(a+n//3*2, n//3)

for s in stdin:
    s = s.strip()
    if not s:
        continue
    N = int(s)
    line = ['-'] * (3 ** N)
    if N > 0:
        cut_line(0, 3 ** N)
    print(''.join(line))



#    while True:
 #   try:
  #      s = input()
   # except EOFError:
    #    break           # no more input
    ##if s == "":         # user pressed Enter on empty line
     #   break
    #print("got:", s)