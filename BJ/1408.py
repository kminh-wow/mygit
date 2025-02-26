n = int(input())  
for _ in range(n):  
    p = int(input())  
    max_value = float('-inf')  # 현재 최대값 저장 (-무한대로 초기화)
    max_name = ""  

    for _ in range(p):  
        num, name = input().split()  
        num = int(num)  

        if num > max_value:  
            max_value = num
            max_name = name

    print(max_name) 