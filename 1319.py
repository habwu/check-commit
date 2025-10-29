1319
def solve():
    n = int(input())
    grid = [[0] * n for _ in range(n)]
    numbers = {}
    k = 1

    for d in range(2*n -1):
      for x in range(n):
        y = d - x
        if 0 <= y < n:
          numbers[(x,y)] = k
          k+=1

    for i in range(n):
      for j in range(n):
        x = i
        y = n-1-j
        grid[i][j] = numbers[(x,y)]


    for row in grid:
        print(*row)
solve()
