array = []
temp = 0
for i in range(5):
    array.append(list(input()))
    if temp < len(array[i]) : temp = len(array[i])

for i in range(temp):
    for j in range(5):
        try:
            print(array[j][i],end = "")
        except:
            continue
