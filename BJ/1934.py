import math

def lcm(a, b):
    return (a * b) // math.gcd(a, b)  # 최소공배수 공식 적용

t = int(input())

for _ in range(t):
    a1, b1 = map(int, input().split())
    print(lcm(a1, b1))
v