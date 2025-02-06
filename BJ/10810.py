n,m = map(int, input().split())
array_a = [0] * (n)

for l in range(m):
    i,j,k = map(int, input().split())
    for a in range(i,j+1):
        array_a[a-1] = k
    
for _ in range(len(array_a)):
    print(array_a[_], end= " ")
