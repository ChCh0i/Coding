diar = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']

count = 0

for i in input():
    for j in diar:
        if i in j:
            count += diar.index(j)+3
print(count)

