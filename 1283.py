from math import *
start,finish,procent=map(int,input().split())
if start <= finish:
    print(0)
else:
    print(ceil(log(finish/start, (100-procent)/100.0)))
