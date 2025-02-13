arr = [[],[],[],[],[]]

for i in range(5):
    a = list(str(input()))
    arr[i][i].append(a[i])
    
print(arr)