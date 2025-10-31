s = input().strip()
n = len(s)
max_count = 0
best_sub = ""
for i in range(n):
    for j in range(i, n):
        sub = s[i:j+1]
        count = 0
        for k in range(n - len(sub) + 1):
            if s[k:k+len(sub)] == sub:
                count += 1
        if count > max_count or (count == max_count and sub < best_sub):
            max_count = count
            best_sub = sub
print(best_sub)
