number = int(input())
arr = [input() for _ in range(number)]

for i in range(number):
    print(arr[i][0],arr[i][-1],sep='')
