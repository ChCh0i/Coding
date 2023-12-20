string = input()

arr = [chr(code) for code in range(97,123)]
str = ''.join(arr)

for i in str:
    if i in string:
        print(string.index(i), end=' ')
    else:
        print(-1,end=' ')
