a = []
for _ in range(4):
    a.append(input())
b = []
for _ in range(4):
    b.append(input())
res = ""
for _ in range(4):
    for r in range(4):
        for c in range(4):
            if a[r][c] == 'X':
                res += b[r][c]
    c = [""] * 4
    for i in range(4):
        c[i] = "".join([a[3-j][i] for j in range(4)])
    a = c
print(res)
