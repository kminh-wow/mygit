N = int(input())


if N == 1:
    exit()


factor = 2
while N > 1:
    if N % factor == 0:  
        print(factor)  
        N //= factor  
    else:
        factor += 1 