N, B = input().split()
B = int(B)

spell = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
c=0 # 자리수    
r=0
for i in (reversed(N)):
    if i in spell:
        r += (spell.index(i)+10)*(B**c) #A는 10부터 시작하므로
    else:
        r+=(int(i))*(B**c)
    c+=1

print(r)