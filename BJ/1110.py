n = int(input())
num = n
i=0
while True:
    a = n//10
    b = n%10
    c = (a+b)%10
    n = b*10 + c
    i+=1
    if n == num:
        print(i)
        break



        
        