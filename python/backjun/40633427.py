cycle = int(input())

for x in range(cycle):
  b, y = map(int, input().split())
  x+=1
  print(f'Case #{x}: {b} + {y} = {b+y}')
