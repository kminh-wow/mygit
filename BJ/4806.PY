while True:
    a,b,c = map(int, input().split())
    if a==0 and b==0 and c==0:
        break
    else:
        if c / b == b / a:
            print('GP', c*(b//a))
        elif c-b == b-a:
            print('AP', c+(b-a))
                