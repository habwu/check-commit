
x, y, c = map(int, input().split())
if x + y < c:
    print("Impossible")
else:
    a = min(x, c)
    b = c - a
    if b <= y:
        print(a, b)
    else:
        b = y
        a = c - b
        print(a, b)
