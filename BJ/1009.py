t = int(input())


last_digit_patterns = {
    0: [10],      
    1: [1],      
    2: [2, 4, 8, 6],
    3: [3, 9, 7, 1],
    4: [4, 6],
    5: [5],
    6: [6],
    7: [7, 9, 3, 1],
    8: [8, 4, 2, 6],
    9: [9, 1]
}

for i in range(t):
    a, b = map(int, input().split())
    last_digit = a % 10
    pattern = last_digit_patterns[last_digit]
    cycle_length = len(pattern)
    
    
    index = (b - 1) % cycle_length 
    print(pattern[index])