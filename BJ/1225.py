a,b = map(str, input().split())

s= 0

a = list(a)
b = list(b)

for i in range(len(a)):
    for j in range(len(b)):
        s+=(int(a[i])*int(b[j]))
        
print(s)