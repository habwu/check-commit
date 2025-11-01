n = int(input())
matrix = []
for _ in range(n):
 row = list(map(int, input().split()))
 matrix.append(row)
result = []
for s in range(2 * (n - 1) + 1):
 for i in range(n - 1, -1, -1):
 j = s - i
 if 0 <= j < n:
 result.append(str(matrix[i][j]))
print(' '.join(result))
