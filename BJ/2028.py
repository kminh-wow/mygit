t = int(input())

for i in range(t):
    n = int(input())
    nn = n**2
    if n%10 == n:
        if nn%10 == n:
            print('YES')
        else:
            print('NO')
    else:
        if nn%100 == n:
            print('YES')
        else:
            print('NO')