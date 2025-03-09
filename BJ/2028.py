t = int(input())

for _ in range(t):
    n = int(input())
    nn = n ** 2  

    
    num_digits = len(str(n))  
    last_digits = nn % (10 ** num_digits) 
    
    if last_digits == n:
        print("YES")
    else:
        print("NO")
