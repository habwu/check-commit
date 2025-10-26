def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    unused_booms = 0
    alive_droids = 0
    
    for booms in a:
        if booms > k:
            unused_booms += booms - k
        else:
            alive_droids += k - booms
            
    print(unused_booms, alive_droids)

solve()
