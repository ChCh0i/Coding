n = int(input())
count = 1

for i in reversed(range(n)):
    if i != 0:
        print(" "*(i-1),end=' ')
    print("*"*count)
    count+=2
    
for j in range(n):
    count-=2
    if j != 0:
        print(" "*(j-1),end=' ')
        print("*"*count)
    
