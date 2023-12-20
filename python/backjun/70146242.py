array = []
temp = 0
temp2 = 0

for i in range(9):
    array.append(list(map(int,input().split())))
    
    if temp < max(array[i]) : 
        temp = max(array[i])
        temp2 = i

print(temp)
print(temp2+1,array[temp2].index(temp)+1)
