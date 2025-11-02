
def solve():
    n, m, y = map(int, input().split())
    
    solutions = []
    for x in range(0, m):
        if pow(x, n, m) == y:
            solutions.append(x)
            
    if len(solutions) == 0:
        print("-1")
    else:
        print(*solutions)

solve()
