que = []



def push(x):
    que.append(x)
    
def pop():
    if len(que) == 0:
        print('-1')
    else:
        print(que[0])
        que.pop[0]
        
def size():
    print(len(que))
    
def empty():
    if len(que) == 0:
        print('1')
    else:
        print('0')

def front():
    if len(que) == 0:
        print('-1')
    else:
        print(que[0])

def back():
    if len(que) == 0:
        print('-1')
    else:
        print(que[-1])
        

n = int(input())

for i in range(n):
    x = list(input().split())
    if x[0] == 'push':
        push(int(x[1]))
    elif x[0] == 'front':
        front()
    elif x[0] == 'pop':
        pop()
    elif x[0] == 'size':
        size()
    elif x[0] == 'empty':
        empty()
    elif x[0] == 'back':
        back()
    
    