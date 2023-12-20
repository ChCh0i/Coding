n, m = map(int,input().split())

arr = list(range(1,n+1))
for _ in range(m):
    i, j = map(int,input().split())
    temp = arr[i-1:j]
    arr[i-1:j] = temp[::-1]

for i in range(n):
    print(arr[i],end=" ")
