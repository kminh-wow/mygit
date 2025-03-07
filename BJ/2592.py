l = [0,0,0,0,0,0,0,0,0]
s=0
for _ in range(10):
    n = int(input())
    s+=n
    l[n//10]+=1

print(int(s/10))
print(max(l))
