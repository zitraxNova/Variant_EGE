def Del(n, m):
    return n % m == 0

for a in range(1, 10000):
    k = 1
    for x in range(1, 10000):
        f = (not Del(x, a)) <= (Del(x, 48) <= (not Del(x, 173)))
        if not f:
            k = 0
            break
    if k:
        print(a)
        
# 8304