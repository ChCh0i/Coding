score = ["A+","A0","B+","B0","C+","C0","D+","D0","P","F"]
number = 4.5
arr = []
cnt = []

for _ in range(20):
    name,s,s1 = input().split()
    if score.index(s1) < 8:
        arr.append(float(s)*(number - 0.5*score.index(s1)))
        cnt.append(float(s))
    elif score.index(s1) == 9:
        arr.append(float(s)*0.0)
        cnt.append(float(s))

print(round(sum(arr)/sum(cnt),6))

