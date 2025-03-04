import math
ans = []

def is_prime_number(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False 
    return True

m = int(input())
n = int(input())

for i in range(m,n+1):
    if is_prime_number(i) == True:
        ans.append(i)

if len(ans) != 0:
    print(sum(ans))
    print(ans[0])
else:
    print('-1')