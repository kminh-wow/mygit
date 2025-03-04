T = int(input()) 
for _ in range(T):
    N = int(input())  
    sumc = 0  
    sumgpa = 0  
    
    for _ in range(N):
        c, g = input().split()
        c = int(c)  
        g = float(g)  
        sumc += c  
        sumgpa += c * g  
    
    print(sumc, round(sumgpa / sumc, 1)) 