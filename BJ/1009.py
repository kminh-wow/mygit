t = int(input())

for i in range(t):
    a,b = map(int, input().split())
    c = list(map(int,str(a**b)))
    if c[-1] == 0:
        print('10')
    else:
        print(c[-1])